# TemporaryAccessPass


## Admin registered temporary access pass method for user

```kql
AuditLogs 
| where ResultDescription == "Admin registered temporary access pass method for user"
 
AuditLogs 
| where ResultDescription == "Admin registered temporary access pass method for user"
| project ResultDescription, Result, ResultReason, InitiatedBy=parse_json(InitiatedBy)[0].userPrincipalName 
 
AuditLogs 
| where ResultDescription == "Admin registered temporary access pass method for user"
| project ActivityDisplayName, InitiatedBy, ResultReason 
| extend UPN=parse_json(InitiatedBy)
```
