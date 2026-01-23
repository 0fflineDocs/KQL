# Applications


## Creates a list of your applications and summarizes successful signins by members vs guests

```kql
let timerange=30d;
SigninLogs
| where TimeGenerated > ago(timerange)
| project TimeGenerated, UserType, ResultType, AppDisplayName
| where ResultType == 0
| summarize
    MemberSignins=countif(UserType == "Member"),
    GuestSignins=countif(UserType == "Guest")
    by AppDisplayName
| sort by AppDisplayName
```


## Applications - total sign ins to each vs distinct sign ins

```kql
SigninLogs
| where TimeGenerated > ago(30d)
| where ResultType == 0
| summarize ['Total Signins']=count(), ['Distinct User Signins']=dcount(UserPrincipalName) by AppDisplayName | sort by ['Distinct User Signins'] desc 
```


## Applications - Members vs guests, per application

```kql
SigninLogs
| where TimeGenerated > ago(30d)
| where ResultType == 0
| summarize ['Distinct Member Signins']=dcountif(UserPrincipalName, UserType == "Member"), ['Distinct Guest Signins']=dcountif(UserPrincipalName, UserType == "Guest")  by AppDisplayName | sort by ['Distinct Guest Signins'] 
```


## Recently created Entra ID principals created by new user accounts

```kql
let NewUsers = AuditLogs
    | where OperationName == "Add user"
    | extend UserID = tostring(TargetResources[0].id)
    | project NewUser = TargetResources[0].userPrincipalName, UserID, UserCreated = TimeGenerated;
let NewServicePrincipals = AuditLogs
    | where OperationName == "Add service principal"
    | project ServicePrincipalDisplayName = TargetResources[0].displayName, ServicePrincipalCreated = TimeGenerated, InitiatedBy = InitiatedBy.user.userPrincipalName;
NewServicePrincipals
    | extend InitiatedBy = tostring(InitiatedBy)
    | join kind=inner (
        NewUsers
        | extend NewUser = tostring(NewUser)
    ) on $left.InitiatedBy == $right.NewUser
    | project ServicePrincipalDisplayName, ServicePrincipalCreated, InitiatedBy, UserCreated, UserID
    | order by ServicePrincipalCreated
```


## Roles added to Service Principals

```kql
AuditLogs
| where TimeGenerated > ago(60d)
| where OperationName == "Add member to role"
| extend ServicePrincipalType = tostring(TargetResources[0].type)
| extend ServicePrincipalObjectId = tostring(TargetResources[0].id)
| extend RoleAdded = tostring(parse_json(tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[1].newValue)))
| extend ServicePrincipalName = tostring(TargetResources[0].displayName)
| extend Actor = tostring(parse_json(tostring(InitiatedBy.user)).userPrincipalName)
| extend ActorIPAddress = tostring(parse_json(tostring(InitiatedBy.user)).ipAddress)
| where ServicePrincipalType == "ServicePrincipal"
| project TimeGenerated, OperationName, RoleAdded, ServicePrincipalName, ServicePrincipalObjectId, Actor, ActorIPAddress
```


## API permissions added to SPs

```kql
AuditLogs
| where TimeGenerated > ago(60d)
| where OperationName == "Add app role assignment to service principal"
| extend AppRoleAdded = tostring(parse_json(tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[1].newValue)))
| extend ActorIPAddress = tostring(parse_json(tostring(InitiatedBy.user)).ipAddress)
| extend Actor = tostring(parse_json(tostring(InitiatedBy.user)).userPrincipalName)
| extend ServicePrincipalObjectId = tostring(parse_json(tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[3].newValue)))
| extend ServicePrincipalName = tostring(parse_json(tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[4].newValue)))
| project TimeGenerated, OperationName, AppRoleAdded, ServicePrincipalName, ServicePrincipalObjectId,Actor, ActorIPAddress
```


## Recent Highly Privileged Application Permissions Consented

```kql
let HighPermissions = dynamic(["AppRoleAssignment.ReadWrite.All", "RoleManagement.ReadWrite.Directory", "Sites.FullControl.All", "Mail.ReadWrite.All"]);
let detectionTime = 1d;
AuditLogs
| where TimeGenerated > ago(detectionTime)
| where OperationName =~ "Consent to application"
| mv-apply TargetResource = TargetResources on
(where TargetResource.type =~ "ServicePrincipal"
| extend AppDisplayName = tostring(TargetResource.displayName),
AppClientId = tostring(TargetResource.id),
props = TargetResource.modifiedProperties)
| mv-apply ConsentFull = props on
(where ConsentFull.displayName =~ "ConsentAction.Permissions")
| mv-apply AdminConsent = props on
(where AdminConsent.displayName =~ "ConsentContext.IsAdminConsent")
| parse ConsentFull with * "ConsentType: " GrantConsentType ", Scope: " GrantScope1 "]" *
| where ConsentFull has_any (HighPermissions)
```
