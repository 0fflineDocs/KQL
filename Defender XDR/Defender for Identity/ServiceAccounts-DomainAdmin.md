# ServiceAccounts DomainAdmin


## Service Accounts in Domain Admins (Defender for Identity)

```kql
let timeframe = 30d; let srvc_list = dynamic(["svc_account1@contoso.com","svc_account2@contoso.com","svc_account3@contoso.com","svc_account4@contoso.com","svc_account5@contoso.com","svc_account6@contoso.com"]); 
IdentityLogonEvents 
| where Timestamp >= ago(timeframe) 
| where AccountUpn in~ (srvc_list) 
| summarize Count = count() by AccountName, DeviceName, Protocol
```
