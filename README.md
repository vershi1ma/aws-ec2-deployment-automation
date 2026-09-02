# AWS EC2 Deployment & Automation

## Overview
Deployed, secured, automated, and scaled a web server on AWS EC2 — progressing from
a single manually-configured instance to a self-healing, load-balanced, HTTPS-secured
web tier, entirely using free-tier and free-cost resources.

## Architecture
A web tier running on Amazon Linux 2023, originally a single manually-configured
instance, later extended with a reusable Launch Template, an Auto Scaling Group
(1-3 instances across multiple Availability Zones), and an Application Load Balancer.
Traffic is served over HTTPS using a free domain and a Let's Encrypt certificate.
Access is via AWS Systems Manager Session Manager (IAM role-based, no open SSH port).

## Skills demonstrated
IAM · EC2 · Security Groups & Network ACLs · EBS (volumes, snapshots) · Elastic IPs ·
Bash scripting (user data) · Custom AMIs & Launch Templates · Auto Scaling Groups
(self-healing infrastructure) · Application Load Balancers & Target Groups ·
CloudWatch metrics & alarms · EC2 cost models (On-Demand vs Spot) · DNS · TLS/SSL
certificate issuance (Let's Encrypt/ACME) · Apache configuration · Linux system
administration and dependency troubleshooting

## Detailed write-ups
- [Core Deployment & Security](docs/01-core-deployment.md)
- [Automation & Golden Images](docs/02-automation-and-golden-images.md)
- [Auto Scaling & Load Balancing](docs/03-auto-scaling-and-load-balancing.md)
- Module 9 — Security Deep-Dive
  - [HTTPS with a Free Domain and Let's Encrypt](docs/09-security-deep-dive/01-https-lets-encrypt.md)
  - [CloudTrail (Audit Logging)](docs/09-security-deep-dive/02-cloudtrail.md)
  - [Encryption at Rest (KMS, S3, EBS)](docs/09-security-deep-dive/03-encryption-at-rest.md)

Each write-up covers what was built and the real problems hit and fixed along the way.
