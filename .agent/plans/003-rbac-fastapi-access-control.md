# Task 003: RBAC FastAPI Access Control

## Objective
Complete Casbin RBAC and FastAPI endpoints so each mock role receives the correct patient-data access.

## Dependencies
- Task 001
- Task 002 for anonymized patient endpoint behavior

## Files Likely Touched
- `medviet-governance/src/access/rbac.py`
- `medviet-governance/src/access/policy.csv`
- `medviet-governance/src/api/main.py`

## Implementation Notes
- Parse `Authorization: Bearer <token>` and return `401` for missing or invalid tokens.
- Use `current_user["username"]` as the Casbin subject: `enforcer.enforce(username, resource, action)`.
- Keep `model.conf` unchanged so existing `g, alice, admin` role inheritance works.
- Add required `policy.csv` permissions: `p, admin, training_data, read`, `p, admin, aggregated_metrics, read`, and `p, ml_engineer, aggregated_metrics, read`.
- Return `403` when a valid role lacks permission.
- Implement raw, anonymized, aggregated metrics, delete, and health endpoints.
- Ensure raw patient data is admin-only.

## Acceptance Criteria
- [x] Missing or invalid tokens return `401`.
- [x] `token-alice` can read raw patient data and delete patients.
- [x] `token-bob` cannot read raw patient data or delete patients.
- [x] `token-alice` and `token-bob` can read anonymized patient data.
- [x] `token-carol` can read aggregated metrics.
- [x] `token-dave` cannot read production, raw, or anonymized patient endpoints.
- [x] Authorized users can read only the resources permitted by policy.
- [x] API responses are valid JSON and do not expose raw PII through anonymized or metrics endpoints.

## Verification
- [x] Run FastAPI checks with `TestClient`.
- [x] Check `token-bob` on `/api/patients/raw` returns `403`.
- [x] Check `token-alice` on `/api/patients/raw` returns `200`.
- [x] Check `token-alice` and `token-bob` on `/api/patients/anonymized` return `200`.
- [x] Check `token-carol` on `/api/metrics/aggregated` returns `200`.
- [x] Check `token-dave` on raw, anonymized, and production patient endpoints returns `403`.
- [x] Check `token-bob` on `DELETE /api/patients/{patient_id}` returns `403`.

## Progress Notes
- Implemented Casbin subject checks using usernames and updated policy coverage for admin and ml_engineer.
- Verified API authorization with FastAPI `TestClient`.
- Observed expected status codes: `bob_raw 403`, `alice_raw 200`, `alice_anon 200`, `bob_anon 200`, `carol_metrics 200`, `dave_anon 403`, `bob_delete 403`.
- Latest scan confirmed the same expected RBAC status codes.

## Status
Completed.
