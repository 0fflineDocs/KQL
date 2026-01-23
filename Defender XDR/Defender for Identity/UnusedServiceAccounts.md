# UnusedServiceAccounts


## Detect potentially unused service accounts

```kql
let timeframe = 30d;
let accounts = dynamic(["svc_account1@contoso.com", "svc_account2@contoso.com"]);
IdentityLogonEvents
| where Timestamp >= ago(timeframe)
| where AccountUpn in (accounts)
| summarize AuthCount=count() by AccountUpn
| where AuthCount == 0
```
