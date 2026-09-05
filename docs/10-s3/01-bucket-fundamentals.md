# 01 — S3 Bucket Fundamentals

## What this covers
Core S3 concepts: buckets, objects, key-based "folders," and storage
classes.

## What I did
- Created an S3 bucket (globally unique name, eu-north-1, public access
  blocked, ACLs disabled)
- Uploaded an object via CLI, verified via console
- Created a "folder" via console and confirmed it's actually just a key
  prefix (and, underneath, a real zero-byte placeholder object)
- Uploaded a second object using the Standard-IA storage class instead
  of the default Standard class
- Cleaned up all test objects and the folder placeholder object

## Key takeaway
S3 has no real filesystem -- "folders" are a UI convenience over flat
object keys containing `/`. Storage class is chosen per-object at
upload time and directly affects cost: Standard for frequently accessed
data, Standard-IA for infrequent access, Glacier for long-term archives.
