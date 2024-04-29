**// Agregate Attack Surface Reduction rules events in M365 Defender Advanced Hunting, in 1h time chunks to display in time line chart**

`DeviceEvents
| where ActionType startswith "Asr"
| summarize count() by ActionType, bin(Timestamp, 1h)
| render timechart`

**// Count Attack Surface Reduction rules events**

`DeviceEvents
| where ActionType startswith "Asr"
| summarize count() by ActionType
| order by count_ desc`
  
**// Get latest events for a specific Attack Surface Reduction rule** 
DeviceEvents| where ActionType == "AsrOfficeCommAppChildProcessAudited" 
  
**// Get stats on ASR audit events - count events and machines per rule**
DeviceEvents 
| where ActionType startswith "Asr" and ActionType endswith "Audited" 
| summarize EventCount=count(), MachinesCount=dcount(DeviceId) by ActionType 
  
**// Get stats on ASR blocks - count events and machines per rule** 
DeviceEvents 
| where ActionType startswith "Asr" and ActionType endswith "Blocked" 
| summarize EventCount=count(), MachinesCount=dcount(DeviceId) by ActionType 
  
**// View ASR audit events - but remove repeating events (e.g. multiple events with same machine, rule, file and process)**
DeviceEvents 
| where ActionType startswith "ASR" and ActionType endswith "Audited" 
| summarize Timestamp =max(Timestamp) by DeviceName, ActionType,FileName, FolderPath, InitiatingProcessCommandLine, InitiatingProcessFileName, InitiatingProcessFolderPath, InitiatingProcessId, SHA1 

**// View executed ASR events, include folder path and initiating process path**
DeviceEvents
| where (Actiontype startswith "AsrOfficeMacro")
| extend RuleId=extractjson("$Ruleid", AdditionalFields, typeof(string))
| project DeviceName, FileName, FolderPath, ProcessCommandLine, InitiatingProcessFileName, InitiatingProcessCommandLine
