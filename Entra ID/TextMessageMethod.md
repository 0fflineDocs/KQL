# TextMessageMethod


## All Members with text message as MFA-method

```kql
SigninLogs
| where UserType == 'Member'
| where parse_json(AuthenticationDetails)[1].authenticationMethod == "Text message"
| project TimeGenerated, UserPrincipalName, AppDisplayName, ResourceDisplayName, PrimaryAuthMethod=parse_json(AuthenticationDetails)[0].authenticationMethod, SecondaryAuthMethod=parse_json(AuthenticationDetails)[1].authenticationMethod
| order by TimeGenerated desc
| summarize count() by UserPrincipalName
```


## All Guests with text message as MFA-method

```kql
SigninLogs
| where UserType == 'Guest'
| where parse_json(AuthenticationDetails)[1].authenticationMethod == "Text message"
| project TimeGenerated, UserPrincipalName, AppDisplayName, ResourceDisplayName, PrimaryAuthMethod=parse_json(AuthenticationDetails)[0].authenticationMethod, SecondaryAuthMethod=parse_json(AuthenticationDetails)[1].authenticationMethod
| order by TimeGenerated desc
| summarize count() by UserPrincipalName
```
