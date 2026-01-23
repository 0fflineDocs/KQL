# SuspiciousCommandLine


## Suspicious command line events


## 'Hunt for unauthorized usage of SSH in your network. SSH should not run as "NT AUTHORITY\System".'

```kql
DeviceProcessEvents
| where InitiatingProcessCommandLine in ("ssh", "-p 443")
| where AccountSid == "S-1-5-18"
| project TimeGenerated, DeviceId, DeviceName, AccountName, InitiatingProcessCommandLine, InitiatingProcessFolderPath, InitiatingProcessFileName
| order by TimeGenerated desc
```
