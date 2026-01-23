# DisabledAccounts


## Find out what users are disabled.

```kql
IdentityInfo | where IsAccountEnabled == “0” | summarize arg_max(AccountName,*) by AccountUpn
```
