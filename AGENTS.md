# Agent Instructions

## Scope
These instructions apply to the entire repository. The application code lives in `medviet-governance/`; run project commands from that directory unless a task plan says otherwise.

## Workflow
- Before executing lab tasks, use the project-local venv at `medviet-governance/.venv`.
- If the venv does not exist, create it and install `requirements.txt` plus `vi_core_news_lg` before implementation.
- Inspect the relevant source, tests, and plan file before editing.
- Keep changes small and aligned with the active task plan in `.agent/plans/`.
- Update `.agent/PLANS.md` and the relevant task plan when task status changes.
- Prefer focused implementation sessions that leave the project in a verifiable state.
- Do not perform unrelated refactors while completing lab tasks.

## Verification
- Run targeted tests after each task.
- Use `pytest tests/test_pii.py -v --tb=short` for PII and anonymization work.
- Use FastAPI/curl checks for RBAC endpoint behavior.
- Use round-trip Python checks for encryption work.
- Record important verification commands and results in the relevant plan file.

## Security And Data Handling
- Do not commit `.vault_key`, credentials, secrets, or real patient data.
- Do not include `data/raw/` in final submission artifacts.
- Treat generated reports as reviewable artifacts; inspect security scan output before packaging.
- Keep fake credential tests temporary and ensure they are not committed.
