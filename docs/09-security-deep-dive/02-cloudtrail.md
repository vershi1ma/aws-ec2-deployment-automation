# 02 — CloudTrail (Audit Logging)

## What this covers
Enabling AWS CloudTrail to log account activity for audit and
security-investigation purposes.

## What I did
- Created a real CloudTrail trail (not just the default 90-day event history)
- Configured it to deliver logs to a dedicated S3 bucket
- Verified log delivery by checking the bucket for incoming log files

## Why it matters
Without an active trail, AWS only retains ~90 days of management events
and doesn't guarantee delivery to a durable store. A configured trail
with S3 delivery gives a permanent, queryable audit record — critical
for any security or compliance-driven environment, and the same data
source used later to verify KMS key usage (see encryption-at-rest doc).

## Key takeaway
Logging isn't automatically "on" in a durable sense by default — a
trail has to be deliberately created and pointed at storage you control.
