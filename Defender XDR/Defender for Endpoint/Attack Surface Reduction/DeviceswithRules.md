# DeviceswithRules


## View All devices, their OS platform and status of each ASR-Rule applied to them

```kql
DeviceInfo
| where OnboardingStatus == 'Onboarded'
| where isnotempty(OSPlatform)
| summarize arg_max(Timestamp, *) by DeviceName
| where OSPlatform startswith "Windows"
| project DeviceName, OSPlatform
| join kind=leftouter (
  DeviceTvmInfoGathering
  | extend AF = parse_json(AdditionalFields)
  | extend ASR1 = parse_json(AdditionalFields.AsrConfigurationStates)
  | project DeviceName, ASR1
  | evaluate bag_unpack(ASR1)
  )
  on $left.DeviceName == $right.DeviceName
  | project-away DeviceName1
```
