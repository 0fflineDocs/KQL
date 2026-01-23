# CountASREvents


## Count Attack Surface Reduction rules events.

```kql
DeviceEvents
| where ActionType startswith "Asr"
| summarize count() by ActionType
| order by count_ desc
```
