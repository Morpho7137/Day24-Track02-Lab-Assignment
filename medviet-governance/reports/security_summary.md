# Security Scan Summary

Generated for the MedViet governance lab submission.

## Results
- Tests: Passed. See `reports/test_results.txt`.
- Bandit SAST: No high, medium, or low severity findings. See `reports/bandit_report.json`.
- pip-audit: No known vulnerabilities reported for audited packages. `vi_core_news_lg` is skipped because it is not published on PyPI.
- TruffleHog: No findings. `reports/trufflehog_report.txt` is intentionally empty because the final scan did not detect secrets.

## Notes
- Local-only artifacts such as `.venv/`, `.vault_key`, raw patient data, caches, and zip files are excluded from the committed repository.
- The generated raw patient dataset is not committed because it contains PII-like fields.
