# 07 — DNS Firewall

## What this covers
Blocking outbound DNS queries to known-malicious domains using Route 53
Resolver DNS Firewall, attached at the VPC level.

## What I did
- Created a DNS Firewall rule group (Foundational tier)
- Added block rules using AWS-managed threat domain lists (Malware,
  Botnet/Command and Control), rather than building a custom domain
  list from scratch
- Set action to BLOCK with NODATA response, so blocked lookups fail
  silently rather than returning an error that reveals filtering
- Associated the rule group with the VPC containing Cloudlearner-server
- Verified association via both console (VPC association status:
  Associated) and CLI (`list-firewall-rule-group-associations`)

## Why it matters
This adds a prevention layer distinct from the rest of Module 9:
CloudTrail records what happened, GuardDuty flags what looks
suspicious, DNS Firewall stops certain malicious connections before
they can even resolve a hostname.

## Cost note
Billed per rule group VPC association and per DNS query volume
processed — for a single small instance, this is a low, ongoing cost
(well under $1/month in practice).

## Key takeaway
A meaningful chunk of malware behavior (command-and-control callbacks,
known malicious domains) can be blocked for near-zero effort using
AWS-managed threat lists, without maintaining a custom blocklist.
