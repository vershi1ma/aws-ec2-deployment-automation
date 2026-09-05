# 08 — Network Firewall

## What this covers
AWS Network Firewall: stateful, packet-level traffic inspection at the
VPC level, and a deliberate decision on when this level of protection
is (and isn't) worth its cost.

## What I did
- Created a dedicated firewall subnet, separate from the instance subnet
- Created a Network Firewall, an empty firewall policy, and a stateful
  domain-list rule group (DENY on a test domain)
- Verified the full chain end-to-end: firewall → policy → rule group,
  all associated with the VPC containing Cloudlearner-server
- Deleted every resource (firewall, policy, rule group, subnet)
  immediately after verification, before any real hourly cost accrued

## Why I didn't leave it running
Network Firewall costs roughly $0.30-0.40/hour per endpoint
(~$250-300/month) plus data processing, and requires rerouting VPC
route tables through firewall subnets to actually filter live traffic.
On a single-instance account, that's a disproportionate cost and an
unnecessary routing change for a learning exercise. The goal here was
understanding the architecture and mechanics, not running it long-term.

## DNS Firewall vs Network Firewall
- DNS Firewall: filters domain name lookups only, cheap, VPC-level
- Network Firewall: filters actual packets (IP/port/protocol/content),
  far more capable, meaningfully more expensive and architecturally
  invasive

## Key takeaway
Knowing when a security tool is disproportionate to the actual
architecture is as important as knowing how to configure it. A single
EC2 instance doesn't need enterprise-grade network inspection running
continuously -- the judgment to build, verify, and tear back down is
itself the demonstrable skill here.
