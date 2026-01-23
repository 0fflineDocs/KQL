# ServiceAccount LoginPattern


## Count all the authentication request that have been made, per day for each associated service account. This will show us a pattern of all the logons a service account has made.

```kql
let timeframe = 30d; let srvc_list = dynamic(["svc_account1@contoso.com","svc_account6@contoso.com"]); 
IdentityLogonEvents 
| where Timestamp >= ago(timeframe) 
| where AccountUpn in~ (srvc_list) 
| summarize Count = count() by bin(Timestamp, 24h), AccountName, DeviceName 
| sort by Timestamp desc
```
