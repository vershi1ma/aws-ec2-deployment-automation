content = open('README.md').read()
old1 = "  - [GuardDuty (Threat Detection)](docs/09-security-deep-dive/06-guardduty.md)"
new1 = old1 + "\n  - [DNS Firewall](docs/09-security-deep-dive/07-dns-firewall.md)"
old2 = "\u00b7 Amazon GuardDuty (threat detection)"
new2 = old2 + " \u00b7 Route 53 Resolver DNS Firewall"
changed = False
if old1 in content:
    content = content.replace(old1, new1)
    changed = True
    print("Write-ups: updated.")
else:
    print("Write-ups: WARNING anchor not found.")
if old2 in content:
    content = content.replace(old2, new2)
    changed = True
    print("Skills: updated.")
else:
    print("Skills: WARNING anchor not found.")
if changed:
    open('README.md', 'w').write(content)
    print("README.md written.")
