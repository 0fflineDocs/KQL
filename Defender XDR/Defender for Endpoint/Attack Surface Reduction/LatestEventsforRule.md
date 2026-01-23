# LatestEventsforRule


## Get latest events for a specific Attack Surface Reduction rule

```kql
DeviceEvents
| where ActionType == "AsrOfficeCommAppChildProcessAudited"
```
