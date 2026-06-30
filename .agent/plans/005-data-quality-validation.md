# Task 005: Data Quality Validation

## Objective
Complete patient data quality checks for anonymized data and provide a validation helper with clear pass/fail output.

## Dependencies
- Task 001
- Task 002

## Files Likely Touched
- `medviet-governance/src/quality/validation.py`

## Implementation Notes
- Build expectations for non-null `patient_id`, CCCD length, lab result range, allowed `benh` values, email format, and unique `patient_id`.
- Implement `validate_anonymized_data(filepath)` returning `{"success": bool, "failed_checks": list, "stats": dict}`.
- Check for nulls in important columns.
- Check row count against original raw data when available.
- Implement `build_patient_expectation_suite()` using the Great Expectations API available in the installed `great-expectations>=0.17.0` package. Prefer `context.sources.pandas_default.read_dataframe(df)` when present; otherwise create an in-memory pandas validator through the installed package's documented pandas datasource/batch API. Keep the public function signature unchanged and document the exact API used in this plan after implementation.

## Acceptance Criteria
- [x] Expectation suite construction runs without syntax errors.
- [x] Validation output includes `success`, `failed_checks`, and `stats`.
- [x] Failed checks are specific enough to diagnose the issue.
- [x] Validation catches missing required values and row count mismatches.

## Verification
- [x] Run a Python import check for `src.quality.validation`.
- [x] Run validation against an anonymized CSV after Task 002 produces one.

## Progress Notes
- Implemented a Great Expectations suite with 6 expectations using the installed GX API.
- Implemented `validate_anonymized_data()` with GX-backed and manual checks.
- Validated `data/processed/patients_anonymized.csv` successfully with `success: True`.
- Latest scan confirmed validation success with no failed checks.

## Status
Completed.
