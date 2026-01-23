# device code usage


## Check Device Code usage - https://cloudbrothers.info/en/protect-users-device-code-flow-abuse/

```kql
SigninLogs
| where TimeGenerated > ago(90d)
| where AuthenticationProtocol == "deviceCode"
| summarize by AppDisplayName, UserId
```
