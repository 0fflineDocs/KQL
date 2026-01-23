# PercentageSignMFA


## Percentage of sign-ins based on MFA

```kql
let timerange=30d;
SigninLogs
| where TimeGenerated > ago(timerange)
| where ResultType == 0
| summarize
    TotalCount=count(),
    MFACount=countif(AuthenticationRequirement == "multiFactorAuthentication"),
    nonMFACount=countif(AuthenticationRequirement == "singleFactorAuthentication")
    by AppDisplayName
| project AppDisplayName, TotalCount, MFACount, nonMFACount, MFAPercentage=(todouble(MFACount) * 100 / todouble(TotalCount))
| sort by MFAPercentage desc
```
