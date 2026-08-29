# AWS EC2 Deployment & Automation

## Overview
Deployed and automated a live web server on AWS EC2 from scratch — covering manual
configuration, infrastructure security, and progressing to fully automated,
template-based server provisioning.

## What was built
- Launched an EC2 instance (Amazon Linux 2023, t3.micro) in a custom security group
- Configured inbound/outbound security group rules (SSH restricted to a single IP, HTTP open publicly)
- Installed and configured Apache manually, and served a custom HTML page
- Connected via AWS Systems Manager Session Manager (IAM role-based access, no SSH keys
  or open SSH port required)
- Took an EBS snapshot for backup/recovery
- Allocated and associated an Elastic IP for a persistent public address
- Wrote a bootstrap (user data) script to fully automate server setup on launch
  (Apache install + config + custom page, zero manual steps)
- Built a custom AMI ("golden image") baking in the fully configured server, and
  proved a new instance launched from it boots ready-to-serve with no script at all
- Created a reusable Launch Template combining AMI, instance type, security group,
  and IAM role for repeatable deployments

## Skills demonstrated
IAM (users, roles, least-privilege policies) · EC2 · Security Groups & Network ACLs ·
EBS (volumes, snapshots) · Elastic IPs · Bash scripting (user data) · AMIs/Launch Templates ·
Linux system administration (Amazon Linux 2023, systemctl, Apache/httpd)

## Real problems hit and fixed (not just a clean tutorial run)
- **SSH connectivity failures**: EC2 Instance Connect repeatedly failed from a mobile
  browser; root-caused to the connection needing to match the client's real-time public
  IP, which changes frequently on cellular data. Solved by switching to Session Manager
  (IAM-based access, no inbound SSH dependency at all).
- **Wrong security group edited**: initially modified a security group not actually
  attached to the running instance; found and fixed by cross-referencing the instance's
  actual attached security group ID.
- **Wrong AWS region**: an Elastic IP allocated in `us-east-1` couldn't attach to an
  instance running in `eu-north-1` — Elastic IPs are region-scoped; reallocated in the
  correct region.
- **Silent user data script failure**: a multi-line bootstrap script failed with
  "No such file or directory" — diagnosed via `/var/log/cloud-init-output.log`, which
  showed all script lines had been collapsed onto a single line by the input method.
  Fixed by joining commands with semicolons instead of relying on line breaks.
- **Session Manager not connecting**: root-caused to no IAM role being attached to the
  instance; fixed by attaching an `AmazonSSMManagedInstanceCore` role and rebooting to
  force the SSM agent to pick up new credentials.

## Architecture
Single EC2 instance in the default VPC, public subnet, Elastic IP attached, Apache
serving HTTP on port 80, Session Manager for shell access via IAM role instead of SSH.
