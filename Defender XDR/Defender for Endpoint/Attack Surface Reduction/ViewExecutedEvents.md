# ViewExecutedEvents


## View executed ASR events, include folder path and initiating process path

```kql
DeviceEvents
| where (Actiontype startswith "AsrOfficeMacro")
| extend RuleId=extractjson("$Ruleid", AdditionalFields, typeof(string))
| project DeviceName, FileName, FolderPath, ProcessCommandLine, InitiatingProcessFileName, InitiatingProcessCommandLine
```
