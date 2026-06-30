# Task 007: OPA Policy And Compliance

## Objective
Complete OPA access rules and the NĐ13/ISO 27001 compliance checklist.

## Dependencies
- Task 003 for aligned RBAC behavior

## Files Likely Touched
- `medviet-governance/policies/opa_policy.rego`
- `medviet-governance/compliance_checklist.md`

## Implementation Notes
- Keep default deny behavior.
- Allow admin all access.
- Allow ML engineer only training data and model artifact read/write as specified.
- Allow data analyst to read aggregated metrics and write reports.
- Allow intern only sandbox access.
- Deny restricted data export outside Vietnam.
- Complete compliance TODOs with concrete technical controls.

## Acceptance Criteria
- [x] OPA policy parses successfully.
- [x] ML engineer delete of production data evaluates as denied.
- [x] Data analyst and intern permissions match lab requirements.
- [x] Restricted data export outside Vietnam is denied.
- [x] Compliance checklist no longer contains unresolved blanks for required lab fields.

## Verification
- [x] Run OPA eval checks for each role when `opa` is available.
- [x] Review `compliance_checklist.md` against the lab grading criteria.

## Status
Completed.
