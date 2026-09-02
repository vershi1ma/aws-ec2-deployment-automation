# 05 — Encryption at Rest (KMS, S3, EBS)

## What this covers
Encrypting data at rest using AWS KMS customer-managed keys (CMKs),
applied to an S3 bucket and an EC2 EBS volume.

## Key concept
AWS uses envelope encryption: a CMK in KMS encrypts a data key, which
in turn encrypts the actual data. The CMK itself never leaves KMS.

- AWS-managed keys: zero setup, no policy control
- Customer-managed keys (CMK): full control over policy, rotation, audit trail

## What I did

### 1. Created a CMK
- KMS → Customer managed keys → created cloudlearner-key
- Symmetric, Encrypt/Decrypt usage
- Scoped key admin/user permissions to my working IAM identity

### 2. Encrypted an S3 bucket
- Created bucket with default encryption set to SSE-KMS
- Selected cloudlearner-key instead of the AWS-managed default
- Verified via object properties: SSE-KMS + correct key ARN shown

### 3. Encrypted an existing EBS volume (can't be done in place)
- Snapshotted Cloudlearner-server's root volume
- Copied the snapshot with "Encrypt this snapshot" enabled, using cloudlearner-key
- Created a new volume from the encrypted snapshot to confirm Encrypted: true
- Deleted the test volume afterward (kept the encrypted snapshot as proof)

### 4. Verified everything via AWS CLI (from iSH on iPad)

    aws kms describe-key --key-id alias/cloudlearner-key
    aws s3api get-bucket-encryption --bucket <bucket-name>
    aws ec2 describe-snapshots --snapshot-ids snap-085388d39af031d05 --query "Snapshots[].[SnapshotId,Encrypted]" --output table

All three confirmed encryption was correctly applied.

## Known gap
Currently operating via AWS root account for CLI/console access.
A dedicated IAM admin user (Veee) hit an unresolved "Access denied"
permissions issue after a password reset -- pending fix. Root access
keys work but aren't least-privilege; this is tracked as a follow-up.

## Key takeaway
Encryption at rest is a launch-time decision for EBS/RDS -- you can't
retroactively encrypt a live resource, only snapshot/copy/recreate it
encrypted. This should be baked into infrastructure-as-code from day one,
not bolted on later.
