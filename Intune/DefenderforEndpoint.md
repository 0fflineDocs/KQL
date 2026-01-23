# DefenderforEndpoint


## Non-secured MDE-devices

```kql
IntuneDeviceComplianceOrg
| where isnotempty(DeviceHealthThreatLevel)
| where DeviceHealthThreatLevel != "Secured"
| project TimeGenerated, DeviceName, DeviceId, OS, UserName, DeviceHealthThreatLevel
```
