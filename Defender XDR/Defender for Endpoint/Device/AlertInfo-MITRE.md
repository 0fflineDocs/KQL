# AlertInfo MITRE


## Organizational based MITRE ATT&CK technique for past 30 days

```kql
AlertInfo
| where Timestamp > ago(30d)
| where ServiceSource in ("AAD Identity Protection", "Microsoft Defender for Endpoint", "Microsoft Defender for Office 365", "Microsoft Defender for Identity", "Microsoft Cloud App Security", "Microsoft 365 Defender")
| where isnotempty(AttackTechniques)
| mv-expand DetailedAttackTechniques= parse_json(AttackTechniques)
| summarize MITRE_ATTACK_list = count() by tostring(DetailedAttackTechniques)
| render columnchart
```


## Organizational based high/medium alerts for MDE/AV/MDO/MDI/MDA/XDR

```kql
AlertInfo
| where Timestamp > ago(30d)
| where Severity in ("Medium", "High")
| summarize 
Endpoints = countif(ServiceSource == "Microsoft Defender for Endpoint"),
Identities = countif(ServiceSource == "Microsoft Defender for Identity" or ServiceSource == "AAD Identity Protection"),
Emails = countif(ServiceSource == "Microsoft Defender for Office 365"),
Applications = countif(ServiceSource == "Microsoft Cloud App Security"),
M365D_XDR = countif(ServiceSource == "Microsoft 365 Defender")
by bin(Timestamp, 1d)
| render timechart 
```
