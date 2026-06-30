# Task 008: Submission Readiness

## Objective
Run final verification, collect required reports, and prepare the lab submission without sensitive or excluded files.

## Dependencies
- Task 001
- Task 002
- Task 003
- Task 004
- Task 005
- Task 006
- Task 007

## Files Likely Touched
- `medviet-governance/reports/`
- Final zip artifact

## Implementation Notes
- Run the full relevant test suite.
- Create `reports/` before redirecting command output.
- Generate test, Bandit, and TruffleHog reports.
- Package only required deliverables.
- Exclude `data/raw/`, `.vault_key`, credentials, and any temporary fake secret files.

## Acceptance Criteria
- [x] Tests pass or any residual failures are documented.
- [x] Security reports are generated where tools are available.
- [x] Submission zip contains `src/`, `tests/`, `policies/`, `data/processed/`, `compliance_checklist.md`, `reports/`, and `requirements.txt`.
- [x] Submission zip excludes raw data, KEK files, and credentials.
- [x] Final zip contents are inspected after creation and excluded paths are absent.

## Verification
- [x] Run: `pytest tests/ -v --tb=short > reports/test_results.txt`
- [x] Run: `bandit -r src/ -f json -o reports/bandit_report.json`
- [x] Run: `trufflehog git file://. --only-verified > reports/trufflehog_report.txt`
- [x] Inspect final zip contents before submission.

## Status
Completed.
