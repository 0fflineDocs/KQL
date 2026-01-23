# MFA Tampering


## Suspicious MFA tampering - altering authentication levels

```kql
CloudAppEvents 
| where Timestamp > ago(1d) 
| where ApplicationId == 11161 
| where ActionType == "Update user." 
| where isnotempty(AccountObjectId) 
| where RawEventData has_all("StrongAuthenticationRequirement","[]") 
| mv-expand ModifiedProperties = RawEventData.ModifiedProperties 
| where ModifiedProperties.Name == "StrongAuthenticationRequirement" and ModifiedProperties.OldValue != "[]" and ModifiedProperties.NewValue == "[]" 
| mv-expand ActivityObject = ActivityObjects 
| where ActivityObject.Role == "Target object" 
| extend TargetObjectId = tostring(ActivityObject.Id) 
| project Timestamp, ReportId, AccountObjectId, ActivityObjects, TargetObjectId
```
