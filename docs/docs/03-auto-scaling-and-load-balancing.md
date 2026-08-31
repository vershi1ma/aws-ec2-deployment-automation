# Auto Scaling & Load Balancing

## What was added
- **Auto Scaling Group** (min: 1, desired: 2, max: 3) that automatically maintains healthy instance count, launching new instances from the Launch Template as needed
- **Application Load Balancer** with a Target Group distributing traffic across all healthy instances behind a single stable DNS endpoint
- Verified self-healing by manually terminating a running instance and observing the ASG automatically detect the loss and launch a replacement within minutes, restoring desired capacity without manual intervention
- Verified load balancing by accessing the site through the Load Balancer's DNS name (rather than any individual instance IP) and confirming successful routing

## Real problem hit and fixed
- Attaching the Auto Scaling Group to an existing Target Group initially created a second, unintended Target Group instead of using the one already wired to the Load Balancer. Diagnosed by comparing registered targets across both Target Groups, corrected by re-editing the ASG to explicitly attach to the existing Target Group, then removed the orphaned one.
