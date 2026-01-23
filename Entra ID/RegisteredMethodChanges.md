# RegisteredMethodChanges


## User registered or deleted security info

```kql
AuditLogs
| where OperationName == "User registered security info" or OperationName == "User deleted security info"
| where TimeGenerated between (datetime("2023-09-01 00:00") .. datetime("2023-09-07 00:00"))
| extend userPrincipalName_ = tostring(parse_json(tostring(InitiatedBy.user)).userPrincipalName)
| project TimeGenerated,userPrincipalName_,ResultDescription,Result
```


## Changes in Entra ID Authentication Methods configuration

```kql
AuditLogs
| where OperationName in ("Authentication Methods Policy Reset", "Authentication Methods Policy Update", "Authentication Strength Combination Configuration Create", "Authentication Strength Combination Configuration Delete", "Authentication Strength Combination Configuration Update", "Authentication Strength Policy Create", "Authentication Strength Policy Delete", "Authentication Strength Policy Update", "Disable Strong Authentication", "Update the company default cross-tenant access setting", "Update security defaults", "Update authorization policy", "Update Sign-In Risk Policy", "Set password policy", "Set domain authentication", "Set device registration policies", "Reveal local administrator password", "Reset the cross-tenant access default setting")
| project TimeGenerated, OperationName, InitiatedByUpn=InitiatedBy.user.userPrincipalName, InitiatedById=InitiatedBy.user.id, TargetResources
| order by TimeGenerated desc
```


## Phone number registered for multiple users

```kql
AuditLogs
| where TimeGenerated > ago (30d)
| where Result == "success"
| where Identity == "Azure Credential Configuration Endpoint Service"
| where OperationName == "Update user"
| extend UserPrincipalName = tostring(TargetResources[0].userPrincipalName)
| extend PhoneNumber = tostring(parse_json(tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[1].newValue))[0].PhoneNumber)
| where isnotempty(PhoneNumber)
| summarize Users=make_set(UserPrincipalName) by PhoneNumber
| extend CountofUsers=array_length(Users)
| where CountofUsers > 1
```
