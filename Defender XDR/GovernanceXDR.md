# GovernanceXDR


## Guests with Entra ID Roles Assigned

```kql
IdentityInfo
| where TimeGenerated > ago(21d)
| summarize arg_max(TimeGenerated, *) by AccountUPN
| where UserType == "Guest"
| where AssignedRoles != "[]" 
| where isnotempty(AssignedRoles)
| project AccountUPN, AssignedRoles, AccountObjectId
```


## Summarize the total count and the list of files downloaded by guests in your Microsoft 365 Tenant

```kql
let timeframe=30d;
IdentityInfo
| where TimeGenerated > ago(21d)
| where UserType == "Guest"
| summarize arg_max(TimeGenerated, *) by AccountUPN
| project UserId=tolower(AccountUPN)
| join kind=inner (
    OfficeActivity
    | where TimeGenerated > ago(timeframe)
    | where Operation in ("FileSyncDownloadedFull", "FileDownloaded")
    )
    on UserId
| summarize DownloadCount=count(), DownloadList=make_set(OfficeObjectId) by UserId
```


## Summarize the total count of files downloaded by each guest domain in your tenant

```kql
let timeframe=30d;
IdentityInfo
| where TimeGenerated > ago(21d)
| where UserType == "Guest"
| summarize arg_max(TimeGenerated, *) by AccountUPN, MailAddress
| project UserId=tolower(AccountUPN), MailAddress
| join kind=inner (
    OfficeActivity
    | where TimeGenerated > ago(timeframe)
    | where Operation in ("FileSyncDownloadedFull", "FileDownloaded")
    )
    on UserId
| extend username = tostring(split(UserId,"#")[0])
| parse MailAddress with * "@" userdomain 
| summarize count() by userdomain
```
