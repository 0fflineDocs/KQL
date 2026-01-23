# AuditsandBlocks


## Get stats on ASR audit events - count events and machines per rule

```kql
DeviceEvents
| where ActionType startswith "Asr" and ActionType endswith "Audited"
| summarize EventCount=count(), MachinesCount=dcount(DeviceId) by ActionType
```


## Get stats on ASR blocks - count events and machines per rule

```kql
DeviceEvents
| where ActionType startswith "Asr" and ActionType endswith "Blocked"
| summarize EventCount=count(), MachinesCount=dcount(DeviceId) by ActionType
```
