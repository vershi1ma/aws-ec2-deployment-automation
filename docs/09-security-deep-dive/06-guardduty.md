# 06 — GuardDuty (Threat Detection)

## What this covers
Enabling AWS GuardDuty, AWS's managed threat detection service, and
reviewing how it surfaces findings.

## What I did
- Enabled GuardDuty (single click — it immediately starts analyzing
  existing CloudTrail, VPC flow, and DNS log data, no new logging
  infrastructure required)
- Generated sample findings to see realistic finding types
  (e.g. unauthorized access attempts, backdoor activity patterns)
  without needing an actual security incident
- Reviewed finding details: severity, affected resource, and reasoning
- Archived all sample findings via console once reviewed, to keep the
  findings dashboard clean of test data

## Why it matters
GuardDuty reuses data already being collected (CloudTrail) rather than
requiring new agents or logging setup, making it close to a "free win"
for any account already doing basic audit logging. It answers the
practical security question: how would you know if something in your
account was compromised?

## Cost note
Free for the first 30 days per account, then billed by log volume
analyzed. For a small single-instance account, ongoing cost is minimal.

## Key takeaway
Threat detection doesn't have to mean building custom alerting — AWS's
managed detection layer sits on top of infrastructure you likely already
have (CloudTrail) and requires near-zero setup to start producing
actionable findings.
