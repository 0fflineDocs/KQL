# Android OSVersions UniqueDevice


## Corporate-Owned Work Profile

```kql
IntuneDevices
| where OS contains "Android (corporate-owned work profile)"
| summarize dcount(DeviceId) by OSVersion
| render columnchart
```


## Fully Managed

```kql
IntuneDevices
| where OS contains "Android (fully managed)"
| summarize dcount(DeviceId) by OSVersion
| render columnchart
```


## Dedicated

```kql
IntuneDevices
| where OS contains "Android (dedicated)"
| summarize dcount(DeviceId) by OSVersion
| render columnchart
```


## Personally-owned Work Profile

```kql
IntuneDevices
| where OS contains "Android (personally-owned work profile)"
| summarize dcount(DeviceId) by OSVersion
| render columnchart
```


## Device Administrator

```kql
IntuneDevices
| where OS contains "Android (device administrator)"
| summarize dcount(DeviceId) by OSVersion
| render columnchart
```
