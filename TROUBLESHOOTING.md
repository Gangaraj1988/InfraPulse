# Troubleshooting Log

## Issue: Application reported DOWN but container running

### Investigation

Checked container status:
docker ps

Checked logs:
docker logs <container>

Checked connectivity:
curl localhost:5000

### Root Cause

Monitoring script was checking HTTPS instead of HTTP

### Resolution

Corrected monitoring endpoint

### Result

Application health correctly reported

