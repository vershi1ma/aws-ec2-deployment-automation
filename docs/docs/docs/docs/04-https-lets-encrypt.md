# HTTPS with a Free Domain and Let's Encrypt

## What was added
- Registered a free subdomain via No-IP (`cloudlearner.ddnsking.com`) and pointed it at the instance's Elastic IP
- Installed Certbot (Let's Encrypt's official client) on the instance from source, resolving missing build dependencies along the way
- Opened port 443 (HTTPS) in the security group
- Issued and installed a real, trusted TLS certificate — verified end-to-end with no browser security warnings

## Real problems hit and fixed
- **Missing build tools**: Certbot's installer failed compiling a dependency (`python-augeas`) because the instance had no C compiler or XML dev headers installed. Diagnosed from the build log, fixed by installing the "Development Tools" package group and the missing `-devel` libraries.
- **No VirtualHost for Certbot to find**: Certbot's Apache plugin requires an explicit VirtualHost block on port 80 to prove domain ownership; the site had been serving content from Apache's default config with no VirtualHost defined. Fixed by writing a proper `/etc/httpd/conf.d/` config file for the domain.
- **Missing SSL module**: the certificate was issued successfully by Let's Encrypt, but Apache couldn't use it because `mod_ssl` wasn't installed, so Certbot's auto-install step failed. Fixed by installing `mod_ssl` and re-running `certbot install` against the already-issued certificate.
