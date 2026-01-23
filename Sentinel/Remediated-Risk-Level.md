# Remediated Risk Level


## https://x.com/ITguySoCal/status/1877982636251201912


## Analytic Rule - Investigate Remediated MFA Claim/Risky Users

```kql

let a=(
AADRiskyUsers
| where RiskLevel in ('medium','high') and RiskDetail !in('adminConfirmedUserCompromised','adminConfirmedSigninCompromised') 
| distinct tolower(UserPrincipalName));
SigninLogs
| where tolower(UserPrincipalName) in (a)
| where RiskLevelDuringSignIn != 'none' and RiskState != 'remediated'
| project TimeGenerated, Identity, Location, LocationDetails,AuthenticationRequirement, ClientAppUsed, RiskState, RiskDetail, RiskEventTypes
```
