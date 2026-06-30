# Task 004: Encryption Vault

## Objective
Complete the local envelope encryption utility so plaintext can be encrypted, decrypted, and applied to DataFrame columns.

## Dependencies
None.

## Files Likely Touched
- `medviet-governance/src/encryption/vault.py`

## Implementation Notes
- Use AES-256-GCM with a generated data encryption key.
- Encrypt the DEK using the local KEK loaded from `.vault_key`.
- Return base64 encoded `encrypted_dek`, `ciphertext`, and `algorithm`.
- Split nonce and ciphertext correctly during decryption.
- Ensure `encrypt_column()` returns a copied DataFrame and JSON payload strings.
- Add `import pandas as pd` at module scope so the existing `pd.DataFrame` annotation is valid.

## Acceptance Criteria
- [x] `encrypt_data()` returns the documented payload shape.
- [x] `decrypt_data(encrypt_data(value)) == value`.
- [x] `encrypt_column()` replaces target column values with encrypted JSON strings.
- [x] `.vault_key` is not committed or included in final submission.

## Verification
- [x] Run a Python round-trip check with `SimpleVault`.
- [x] Run: `python -c "from src.encryption.vault import SimpleVault"`
- [x] Confirm generated `.vault_key` is treated as a local secret.

## Progress Notes
- Implemented envelope encryption, DEK decryption, and dataframe column encryption.
- Verified `SimpleVault` import and encryption round-trip succeeded.
- Latest scan confirmed encryption round-trip succeeded.

## Status
Completed.
