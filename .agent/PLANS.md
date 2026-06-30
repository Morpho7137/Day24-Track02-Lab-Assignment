# MedViet Governance Planning Index

## Project Objective
Complete the MedViet data governance and security lab in small, verifiable tasks covering PII detection, anonymization, RBAC, encryption, quality validation, security scanning, OPA policy, compliance mapping, and final submission.

## Working Directory
Run project commands from:

```powershell
cd D:\Work\Document\lab1\Day24-Track02-Lab-Assignment\medviet-governance
```

## Environment Prerequisite
Before executing any task, create and use a project-local virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m spacy download vi_core_news_lg
```

Verify the venv before starting Task 001:

```powershell
python -c "import pandas, faker, spacy, presidio_analyzer, presidio_anonymizer, casbin, great_expectations"
python -c "import spacy; spacy.load('vi_core_news_lg'); print('vi_core_news_lg ok')"
```

## Task Plans
| Status | Plan | Purpose |
|---|---|---|
| Completed | `.agent/plans/001-data-generation-and-pii-inventory.md` | Generate sample data and identify PII columns. |
| Completed | `.agent/plans/002-pii-detection-and-anonymization.md` | Implement Presidio detection, anonymization, and tests. |
| Completed | `.agent/plans/003-rbac-fastapi-access-control.md` | Implement Casbin RBAC and FastAPI protected endpoints. |
| Completed | `.agent/plans/004-encryption-vault.md` | Complete local envelope encryption utilities. |
| Completed | `.agent/plans/005-data-quality-validation.md` | Implement data quality checks and validation helper. |
| Completed | `.agent/plans/006-security-scanning-and-hooks.md` | Add security scanning workflow and hook checks. |
| Completed | `.agent/plans/007-opa-policy-and-compliance.md` | Complete OPA access policy and compliance checklist. |
| Completed | `.agent/plans/008-submission-readiness.md` | Verify deliverables and package final submission. |

## Definition Of Done
- Relevant TODOs for the active task are completed.
- Acceptance criteria in the task plan are met.
- Targeted verification commands pass or known failures are documented.
- Sensitive artifacts are not introduced into tracked files.
- `.agent/PLANS.md` and the task plan status are updated.

## Latest Verification
- Tasks 1-5 scan completed successfully.
- `pytest tests/test_pii.py -v --tb=short`: 6 passed.
- FastAPI RBAC status checks matched expectations.
- Encryption round-trip succeeded.
- `validate_anonymized_data("data/processed/patients_anonymized.csv")` returned `success: True`.
- Tasks 6-8 scan completed successfully.
- Pre-commit hook, Bandit, pip-audit, and OPA eval now run from the local venv tooling.
- `pip-audit` reports no known vulnerabilities after the venv refresh.

## Cross-Task Risks
- Vietnamese spaCy model availability may block Presidio `PERSON` recognition.
- Great Expectations APIs may differ across installed versions.
- `data/raw/patients_raw.csv` is generated locally and should not be packaged in final submission.
- Keep the venv disposable; toolchain upgrades can be discarded after grading.
- `trufflehog` reports are still expected to include the intentional sample credential from the lab materials.
