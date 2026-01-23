# AdminAccounts ServiceCreation


## Administrator accounts creating services that execute as System.

```kql
DeviceEvents
| where ActionType == "ServiceInstalled"
| where AdditionalFields.ServiceAccount == "system" or AdditionalFields.ServiceAccount == "LocalSystem"
| where InitiatingProcessAccountUpn != ""
| project TimeGenerated, ServiceName=AdditionalFields.ServiceName, ServiceAccount=AdditionalFields.ServiceAccount, DeviceName, DeviceId, FolderPath, FileName, InitiatingProcessAccountUpn, InitiatingProcessAccountName, InitiatingProcessAccountObjectId
| order by TimeGenerated desc
```
