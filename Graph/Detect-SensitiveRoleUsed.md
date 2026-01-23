# Detect SensitiveRoleUsed


## Detect Sensitive Role Used - https://cloudbrothers.info/en/detect-threats-microsoft-graph-logs-part-2/

```kql
let SensitiveMsGraphPermissions = externaldata(AppId: guid, AppRoleId: guid, AppRoleDisplayName: string, Category: string, EAMTierLevelName: string, EAMTierLevelTagValue: string)["https://raw.githubusercontent.com/Cloud-Architekt/AzurePrivilegedIAM/main/Classification/Classification_AppRoles.json"] with (format='multijson')
    | where EAMTierLevelName == "ControlPlane"
    | distinct AppRoleDisplayName;
let HistoricalActivity = MicrosoftGraphActivityLogs
    | where TimeGenerated between (ago(30d) .. startofday(now()))
    | where Roles has_any (SensitiveMsGraphPermissions)
    | extend ObjectId = iff(isempty(UserId), ServicePrincipalId, UserId)
    | extend ObjectType = iff(isempty(UserId), "ServicePrincipalId", "UserId")
    | summarize by ObjectId;
MicrosoftGraphActivityLogs
| where TimeGenerated between (startofday(now()) .. now())
| extend ObjectId = iff(isempty(UserId), ServicePrincipalId, UserId)
| where Roles has_any (SensitiveMsGraphPermissions)
```


## Remove known object ids

```kql
| where ObjectId !in (HistoricalActivity)
```
