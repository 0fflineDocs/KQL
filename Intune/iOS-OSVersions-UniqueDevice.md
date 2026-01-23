# iOS OSVersions UniqueDevice


## iOS/iPadOS

```kql

IntuneDevices
| where OS contains "iOS/iPadOS"
| summarize dcount(DeviceId) by OSVersion
| render columnchart
```
