# Pivot OSVersion


## Pivot table of all Windows OS versions

```kql
DeviceInfo
| where Timestamp > ago(30d)
| where isnotempty(OSBuild)
| summarize arg_max(Timestamp, *) by DeviceName
| where isnotempty(OSPlatform)
| evaluate pivot(OSBuild, count(), OSPlatform)
| where OSPlatform contains "Windows"
| sort by OSPlatform desc
```
