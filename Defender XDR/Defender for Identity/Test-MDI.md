# Test MDI


## Verify Advanced Hunting - Defender for Identity

```kql
IdentityDirectoryEvents
| where TargetDeviceName contains "Domain_Controller_FQDN" 

IdentityInfo 
| where AccountDomain contains "DOMAIN"

IdentityQueryEvents 
| where DeviceName contains "Domain_Controller_FQDN" 
```
