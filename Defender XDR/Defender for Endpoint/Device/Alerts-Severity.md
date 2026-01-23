# Alerts Severity


## Daily alert & severity for MDE/AV

```kql
AlertInfo
| where Timestamp > ago(30d) 
| where ServiceSource == "Microsoft Defender for Endpoint"
| summarize AlertNum = count() by Severity, bin(Timestamp, 1d)
| render timechart
```


## Summarize count of alerts, based on detection, service, category and severity.

```kql
AlertInfo
| where Timestamp > ago(30d)
| summarize count() by DetectionSource, ServiceSource, Category, Severity
| top 10 by count_ desc nulls last
```
