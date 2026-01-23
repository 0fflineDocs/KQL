# ServiceCreation DomainControllers


## Track service creation activities on domain controllers

```kql
IdentityDirectoryEvents 
| where ActionType == "Service creation" 
| extend ServiceName = AdditionalFields["ServiceName"] 
| extend ServiceCommand = AdditionalFields["ServiceCommand"] 
| project Timestamp, ActionType, Protocol, DC = TargetDeviceName, ServiceName, ServiceCommand, AccountDisplayName, AccountSid, AdditionalFields | limit 100
```
