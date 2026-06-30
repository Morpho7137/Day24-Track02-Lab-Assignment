# Task 002: PII Detection And Anonymization

## Objective
Complete Vietnamese PII detection and anonymization so tests prove CCCD, phone, email, and person-like fields are detected and protected.

## Dependencies
- Task 001

## Files Likely Touched
- `medviet-governance/src/pii/detector.py`
- `medviet-governance/src/pii/anonymizer.py`
- `medviet-governance/tests/test_pii.py`

## Implementation Notes
- Implement Presidio recognizers for `VN_CCCD` and `VN_PHONE`.
- Vietnamese phone numbers must match `^0[35789]\d{8}$`.
- Configure spaCy with `vi_core_news_lg`.
- Implement `detect_pii()` for `PERSON`, `EMAIL_ADDRESS`, `VN_CCCD`, and `VN_PHONE`.
- Implement anonymization strategies needed by tests, prioritizing `replace`.
- Replace or anonymize `ho_ten`, `cccd`, `so_dien_thoai`, `email`, `dia_chi`, and `bac_si_phu_trach`.
- Preserve `patient_id`, `benh`, and `ket_qua_xet_nghiem`.
- Leave `ngay_sinh` and `ngay_kham` unchanged for this implementation.

## Acceptance Criteria
- [x] CCCD values with exactly 12 digits are detected.
- [x] Vietnamese phone numbers matching `^0[35789]\d{8}$` are detected.
- [x] Email addresses are detected.
- [x] Detection rate for `ho_ten`, `cccd`, `so_dien_thoai`, and `email` is at least 95%.
- [x] Original CCCD values do not appear in anonymized output.
- [x] Original direct PII values from anonymized columns do not appear in the anonymized DataFrame.
- [x] Non-PII model-training columns remain unchanged.

## Verification
- [x] Run: `pytest tests/test_pii.py -v --tb=short`
- [x] If the spaCy model is missing, run: `python -m spacy download vi_core_news_lg`
- [x] If spaCy model setup fails, document the exact missing dependency and install command.

## Progress Notes
- Implemented Vietnamese CCCD, phone, and email detection with Presidio plus heuristics.
- Implemented dataframe anonymization and detection-rate handling for CSV-loaded identifiers.
- `pytest tests/test_pii.py -v --tb=short` passed: 6 tests passed.
- Latest scan confirmed 6 PII/anonymization tests passed.

## Status
Completed.
