# 05 — Patch Manager

## What this covers
Automating OS-level patch compliance scanning for EC2 instances using
AWS Systems Manager Patch Manager.

## What I did
- Reviewed the default AWS-managed patch baseline for Amazon Linux 2023
  (auto-approves Critical/Security patches after a delay) rather than
  building a custom baseline
- Tagged Cloudlearner-server with `Patch Group = Cloudlearner` so it's
  addressable by Patch Manager
- Ran a **scan-only** patch job (no install, no reboot) via both console
  and CLI (`AWS-RunPatchBaseline` document, `Operation=Scan`)
- Verified compliance results both ways: console compliance dashboard and
  `aws ssm describe-instance-patches`

## Result
Cloudlearner-server came back fully compliant — zero missing patches
against the default baseline. Confirmed via both interfaces.

## Why scan-only
This is the only running instance in the project, so a real
"scan and install" was deliberately avoided — a required patch can
trigger an automatic reboot. In a real environment, validating a patch
baseline via scan/compliance data before authorizing an install is the
standard operational practice, not a shortcut.

## Key takeaway
Patch Manager turns "did you patch this system" from a manual,
easily-skipped task into a scheduled, auditable process — the same
mechanism (SSM Agent) already used for Session Manager access, so no
new agent or setup was required.
