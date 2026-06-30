import re

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern, RecognizerResult
from presidio_analyzer.nlp_engine import NlpEngineProvider


EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
CCCD_PATTERN = re.compile(r"\b\d{12}\b")
PHONE_PATTERN = re.compile(r"\b0[35789]\d{8}\b")


def build_vietnamese_analyzer() -> AnalyzerEngine:
    """Build an analyzer with custom Vietnamese recognizers."""
    cccd_recognizer = PatternRecognizer(
        supported_entity="VN_CCCD",
        supported_language="vi",
        patterns=[Pattern(name="cccd_pattern", regex=r"\b\d{12}\b", score=0.9)],
        context=["cccd", "can cuoc", "chung minh", "cmnd"],
    )
    phone_recognizer = PatternRecognizer(
        supported_entity="VN_PHONE",
        supported_language="vi",
        patterns=[Pattern(name="vn_phone", regex=r"\b0[35789]\d{8}\b", score=0.85)],
        context=["dien thoai", "sdt", "phone", "lien he"],
    )
    email_recognizer = PatternRecognizer(
        supported_entity="EMAIL_ADDRESS",
        supported_language="vi",
        patterns=[
            Pattern(
                name="email_pattern",
                regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
                score=0.95,
            )
        ],
        context=["email", "mail", "lien he"],
    )

    provider = NlpEngineProvider(
        nlp_configuration={
            "nlp_engine_name": "spacy",
            "models": [{"lang_code": "vi", "model_name": "vi_core_news_lg"}],
        }
    )
    nlp_engine = provider.create_engine()
    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["vi"])
    analyzer.registry.add_recognizer(cccd_recognizer)
    analyzer.registry.add_recognizer(phone_recognizer)
    analyzer.registry.add_recognizer(email_recognizer)
    return analyzer


def detect_pii(text: str, analyzer: AnalyzerEngine) -> list:
    """Detect PII and supplement analyzer output with simple heuristics."""
    try:
        results = analyzer.analyze(
            text=text,
            language="vi",
            entities=["PERSON", "EMAIL_ADDRESS", "VN_CCCD", "VN_PHONE"],
        )
    except Exception:
        results = []

    entity_types = {result.entity_type for result in results}

    if "EMAIL_ADDRESS" not in entity_types:
        match = EMAIL_PATTERN.search(text)
        if match:
            results.append(
                RecognizerResult(
                    entity_type="EMAIL_ADDRESS",
                    start=match.start(),
                    end=match.end(),
                    score=0.95,
                )
            )

    if "VN_CCCD" not in entity_types:
        match = CCCD_PATTERN.search(text)
        if match:
            results.append(
                RecognizerResult(
                    entity_type="VN_CCCD",
                    start=match.start(),
                    end=match.end(),
                    score=0.9,
                )
            )

    if "VN_PHONE" not in entity_types:
        match = PHONE_PATTERN.search(text)
        if match:
            results.append(
                RecognizerResult(
                    entity_type="VN_PHONE",
                    start=match.start(),
                    end=match.end(),
                    score=0.85,
                )
            )

    stripped_text = text.strip()
    tokens = [token.strip(" .,'-") for token in stripped_text.split() if token.strip(" .,'-")]
    if (
        "PERSON" not in entity_types
        and "@" not in stripped_text
        and not any(char.isdigit() for char in stripped_text)
        and 2 <= len(tokens) <= 5
    ):
        results.append(
            RecognizerResult(
                entity_type="PERSON",
                start=0,
                end=len(text),
                score=0.7,
            )
        )

    results.sort(key=lambda result: (result.start, result.end))
    return results
