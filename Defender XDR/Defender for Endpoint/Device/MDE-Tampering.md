# MDE Tampering


## MDE Tampering

```kql
DeviceEvents 
| where ActionType == "TamperingAttempt" 
| extend AdditionalInfo = parse_json(AdditionalFields) 
| extend Status = AdditionalInfo.['Status']
| extend Target = AdditionalInfo.['Target']
```


## Counts how many times 'TamperingAttempt' happened to each device.

```kql
DeviceEvents
| whereTimestamp > ago(30d)
| whereActionType == "TamperingAttempt"| summarizeTamperingAttempt = count() byDeviceId, DeviceName
```


## Counts how many times 'TamperingAttempt' occurred and indicates which registry value impacted each device.

```kql
DeviceEvents
| where Timestamp > ago(30d)
| where ActionType == "TamperingAttempt"
| summarize Registry_Value = make_list(RegistryValueName) by DeviceId, DeviceName
```
