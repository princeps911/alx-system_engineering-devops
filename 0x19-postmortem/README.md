# 0x19 - Postmortem Task: Webstack Debugging #1  
_By Princeps_

![Technical Issue Resolution](./postmorterm_technical.webp)

## Issue Summary  
**Outage Duration:** The outage began at 11:45 AM and was resolved by 12:45 PM West African Time.

## Impact  
The website was unreachable for all users due to the server not listening on port 80.

## Root Cause  
The issue stemmed from an incorrect Nginx setup. The site’s configuration in `sites-available` had not been linked to `sites-enabled`, preventing Nginx from properly serving the site despite having a correct configuration.

## Timeline
- **11:45 AM:** The issue was identified when ALX attempted to access the website and found it unresponsive.
- **11:50 AM:** Monitoring alerts confirmed the site was down, prompting the issue escalation.
- **11:55 AM:** Initial diagnostics focused on Nginx configuration files, but no errors were identified in the configurations.
- **12:15 PM:** Further checks revealed that no service was listening on port 80, leading to the discovery that `sites-available` wasn’t linked to `sites-enabled`.
- **12:30 PM:** The correct configuration was linked, and Nginx was restarted to apply the changes.
- **12:45 PM:** The website was back online, resolving the issue.

## Root Cause and Resolution  
### Root Cause  
The failure to link the Nginx configuration from `sites-available` to `sites-enabled` caused the server to not activate the proper settings, rendering the site inaccessible.

### Resolution  
The problem was fixed by linking the configuration file from `sites-available` to `sites-enabled` and restarting the Nginx service.

## Corrective and Preventative Actions  
### Improvements  
- Implement a script or automated process to verify that any new configuration changes are properly linked and active.
- Enhance the monitoring system to detect similar issues more swiftly.

## Task List  
1. Develop and implement a script to automatically link configurations from `sites-available` to `sites-enabled` after changes.
2. Add monitoring checks to ensure Nginx is consistently listening on port 80.

## Example Script  
Here’s an example script that ensures the Nginx configuration is linked and active:

```bash
#!/usr/bin/env bash
# Ensure Nginx is properly configured and listening on port 80

cat /etc/nginx/sites-available/default > /etc/nginx/sites-enabled/default
sudo service nginx restart
```

This script links the correct configuration and restarts Nginx to apply changes.

---

![Nginx Configuration Flow](./postmoterm_flow_chart.webp)
