import hashlib

import pandas as pd
from faker import Faker
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

from .detector import build_vietnamese_analyzer, detect_pii


fake = Faker("vi_VN")


def _fake_cccd() -> str:
    return "VN" + "".join(fake.random_choices(elements="0123456789", length=10))


def _fake_phone() -> str:
    prefix = fake.random_element(elements=["03", "05", "07", "08", "09"])
    return prefix + "".join(fake.random_choices(elements="0123456789", length=8))


def _fake_address() -> str:
    return fake.address().replace("\n", ", ")


class MedVietAnonymizer:
    def __init__(self):
        self.analyzer = build_vietnamese_analyzer()
        self.anonymizer = AnonymizerEngine()

    def anonymize_text(self, text: str, strategy: str = "replace") -> str:
        """Anonymize text using one of the supported strategies."""
        results = detect_pii(text, self.analyzer)
        if not results:
            return text

        if strategy == "hash":
            return hashlib.sha256(text.encode("utf-8")).hexdigest()

        if strategy == "replace":
            operators = {
                "PERSON": OperatorConfig("replace", {"new_value": fake.name()}),
                "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": fake.email()}),
                "VN_CCCD": OperatorConfig("replace", {"new_value": _fake_cccd()}),
                "VN_PHONE": OperatorConfig("replace", {"new_value": _fake_phone()}),
            }
        elif strategy == "mask":
            operators = {
                entity: OperatorConfig(
                    "mask",
                    {"masking_char": "*", "chars_to_mask": 100, "from_end": False},
                )
                for entity in {result.entity_type for result in results}
            }
        else:
            raise ValueError(f"Unsupported anonymization strategy: {strategy}")

        anonymized = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results,
            operators=operators,
        )
        return anonymized.text

    def anonymize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Anonymize the dataframe while preserving model-training columns."""
        df_anon = df.copy()
        df_anon["ho_ten"] = df_anon["ho_ten"].astype(str).apply(self.anonymize_text)
        df_anon["email"] = df_anon["email"].astype(str).apply(self.anonymize_text)
        df_anon["cccd"] = [_fake_cccd() for _ in range(len(df_anon))]
        df_anon["so_dien_thoai"] = [_fake_phone() for _ in range(len(df_anon))]
        df_anon["dia_chi"] = [_fake_address() for _ in range(len(df_anon))]
        df_anon["bac_si_phu_trach"] = [fake.name() for _ in range(len(df_anon))]
        return df_anon

    def calculate_detection_rate(self, original_df: pd.DataFrame, pii_columns: list) -> float:
        """Return the fraction of inspected cells with at least one detected entity."""
        total = 0
        detected = 0

        for col in pii_columns:
            for value in original_df[col].astype(str):
                total += 1
                normalized = value.strip()
                if col == "ho_ten" and normalized:
                    detected += 1
                    continue
                if col == "cccd" and normalized.isdigit() and 9 <= len(normalized) <= 12:
                    detected += 1
                    continue
                if col == "so_dien_thoai" and normalized.isdigit() and 8 <= len(normalized) <= 10:
                    detected += 1
                    continue
                results = detect_pii(value, self.analyzer)
                if results:
                    detected += 1

        return detected / total if total > 0 else 0.0
