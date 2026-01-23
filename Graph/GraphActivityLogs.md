# GraphActivityLogs


## Check Current Requests

```kql
MicrosoftGraphActivityLogs
| extend ParsedUri = tostring(parse_url(RequestUri).Path)
| summarize TotalRequest = count() by ParsedUri
| sort by TotalRequest
```


## Detect GraphActivity joined with SigninLogs - https://cloudbrothers.info/en/detect-threats-microsoft-graph-logs-part-2/

```kql
MicrosoftGraphActivityLogs
| where TimeGenerated > ago(8d)
| extend ObjectId = iff(isempty(UserId), ServicePrincipalId, UserId)
| extend ObjectType = iff(isempty(UserId), "ServicePrincipalId", "UserId")
| join kind=inner (union isfuzzy=true
        SigninLogs,
        AADNonInteractiveUserSignInLogs,
        AADServicePrincipalSignInLogs,
        AADManagedIdentitySignInLogs
    | where TimeGenerated > ago(90d)
    | summarize arg_max(TimeGenerated, *) by UniqueTokenIdentifier
    )
    on $left.SignInActivityId == $right.UniqueTokenIdentifier
| project-reorder TimeGenerated, ObjectType, UserPrincipalName, ObjectId, SignInActivityId, RequestUri, RequestMethod
```
