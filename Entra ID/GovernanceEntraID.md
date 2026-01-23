# GovernanceEntraID


## Global admin sign-ins to cloud applications.

```kql
SigninLogs
| where TimeGenerated > ago(1d)
| where ResultType == 0
| join kind=inner (IdentityInfo)
    on $left.UserId == $right.AccountObjectId
| where AssignedRoles contains "Global Administrator"
| sort by TimeGenerated
| summarize SignIns=count() by GlobalAdminUpn=UserPrincipalName, GlobalAdminId=UserId, Application=AppDisplayName
| order by GlobalAdminId asc
```
