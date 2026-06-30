# Task 006: Security Scanning And Hooks

## Objective
Set up security scan commands and pre-commit checks for secrets, SAST, and dependency vulnerabilities.

## Dependencies
None.

## Files Likely Touched
- `medviet-governance/.github/hooks/pre-commit`
- `medviet-governance/reports/`

## Implementation Notes
- Configure git-secrets patterns for CCCD, passwords, secret keys, and AWS patterns.
- Ensure the hook runs git-secrets, Bandit, and pip-audit.
- Generate Bandit and TruffleHog reports under `reports/`.
- Keep fake secret tests temporary and uncommitted.

## Acceptance Criteria
- [x] Pre-commit hook script exists and is executable where the platform supports it.
- [x] git-secrets blocks a fake credential test.
- [x] Bandit scan can run against `src/`.
- [x] pip-audit can run against installed dependencies.
- [x] Reports are generated for final submission when tools are available.

## Verification
- [x] Run: `bandit -r src/ -ll`
- [x] Run: `pip-audit --desc on`
- [x] Run: `trufflehog git file://. --only-verified`
- [x] Document unavailable tools or installation blockers.

## Status
Completed.
