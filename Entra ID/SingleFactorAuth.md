# SingleFactorAuth


## Single vs Multi-factor Authentication

```kql
SigninLogs
| where TimeGenerated > ago (30d)
| summarize ['Single Factor Authentication']=countif(AuthenticationRequirement == "singleFactorAuthentication"), ['Multi Factor Authentication']=countif(AuthenticationRequirement == "multiFactorAuthentication") by bin(TimeGenerated, 1d)
| render timechart with (ytitle="Count", title="Single vs Multifactor Authentication last 30 days")
```


## Single vs Multi-factor Authentication (Guests)

```kql
SigninLogs
| where UserType == 'Guest'
| where TimeGenerated > ago (30d)
| summarize ['Single Factor Authentication']=countif(AuthenticationRequirement == "singleFactorAuthentication"), ['Multi Factor Authentication']=countif(AuthenticationRequirement == "multiFactorAuthentication") by bin(TimeGenerated, 1d)
| render timechart with (ytitle="Count", title="Single vs Multifactor Authentication last 30 days")
```
