# 04 — Secrets Manager & Parameter Store

## What this covers
Storing and retrieving application secrets and configuration without
hardcoding them into scripts, AMIs, or source code.

## Parameter Store vs Secrets Manager
- **Parameter Store**: free (Standard tier), good for config values and
  simple secrets. No built-in rotation.
- **Secrets Manager**: ~$0.40/secret/month, built for credentials that
  need automatic rotation (e.g. database passwords). Adds real cost, so
  used deliberately rather than by default.

## What I did
- Stored a plain config value in Parameter Store (`String` type)
- Stored a sensitive value as a `SecureString`, encrypted with the same
  customer-managed KMS key (`cloudlearner-key`) used for S3/EBS encryption
- Confirmed decryption is never automatic in either the console or CLI —
  both require an explicit action/flag to reveal plaintext
- Created a Secrets Manager secret (structured JSON credential pair),
  verified retrieval, then deleted it immediately with
  `--force-delete-without-recovery` to avoid the standard 30-day
  recovery-window billing

## Key takeaway
Secrets should never live in code, user-data, or AMIs. Parameter Store
covers most config/secret needs for free; Secrets Manager is worth the
cost specifically when automatic rotation matters (e.g. RDS credentials —
revisited in Module 11).
