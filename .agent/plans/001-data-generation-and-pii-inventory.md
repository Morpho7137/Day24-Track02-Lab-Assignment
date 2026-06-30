# Task 001: Data Generation And PII Inventory

## Objective
Generate the synthetic patient dataset and document which columns contain PII before implementing detection or anonymization.

## Dependencies
Project venv is created, activated, dependencies are installed from `requirements.txt`, and `vi_core_news_lg` is downloaded.

## Files Likely Touched
- `medviet-governance/scripts/generate_data.py`
- `medviet-governance/data/raw/patients_raw.csv`
- This plan file

## Implementation Notes
- Run the generator from `medviet-governance/`.
- Verify `data/raw/patients_raw.csv` exists and contains 200 rows.
- Identify PII columns from the generated schema.
- Direct PII columns are `ho_ten`, `cccd`, `so_dien_thoai`, `email`, `dia_chi`, and `bac_si_phu_trach`.
- Sensitive health/date metadata columns are `ngay_sinh` and `ngay_kham`.
- Preserve as non-direct identifiers or training fields: `patient_id`, `benh`, and `ket_qua_xet_nghiem`.

## Acceptance Criteria
- [x] `data/raw/patients_raw.csv` is generated locally.
- [x] The dataset has the expected columns and 200 patient records.
- [x] PII columns are documented in this plan or a lab report.
- [x] No generated raw data is prepared for final submission.

## Verification
- [x] Confirm venv is active: `python -c "import sys; print(sys.prefix)"`
- [x] Confirm dependencies import successfully: `python -c "import pandas, faker, spacy, presidio_analyzer, presidio_anonymizer, casbin, great_expectations"`
- [x] Confirm spaCy model loads: `python -c "import spacy; spacy.load('vi_core_news_lg'); print('vi_core_news_lg ok')"`
- [x] Run: `python scripts/generate_data.py`
- [x] Inspect row count and columns with Python or pandas.
- [x] Confirm `data/raw/` remains excluded from final packaging.

## Progress Notes
- Generated `data/raw/patients_raw.csv` with 200 rows.
- Confirmed expected patient columns are present.
- Classified direct PII, sensitive metadata, and preserved training fields per plan.

## Status
Completed.
