# Automation & Golden Images

## What was built
- Wrote a bootstrap (user data) script to fully automate server setup on launch (Apache install + config + custom page, zero manual steps)
- Built a custom AMI ("golden image") baking in the fully configured server, and proved a new instance launched from it boots ready-to-serve with no script at all
- Created a reusable Launch Template combining the AMI, instance type, security group, and IAM role for repeatable deployments

## Real problem hit and fixed
- **Silent user data script failure**: a multi-line bootstrap script failed with "No such file or directory" on first launch. Diagnosed via `/var/log/cloud-init-output.log`, which showed all script lines had been collapsed onto a single line by the mobile input method used to type it. Fixed by rewriting the script to join commands with semicolons instead of relying on line breaks, making it immune to how the input method handled line endings.
