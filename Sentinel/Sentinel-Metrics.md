# Sentinel Metrics


## List all incidents

```kql
let startTime = ago(30d);
let endTime = now();
SecurityIncident
| where TimeGenerated >= startTime
| summarize arg_max(TimeGenerated, *) by IncidentNumber
| where LastModifiedTime  between (startTime .. endTime)
| where Status in  ('New', 'Active', 'Closed')
| where Severity in ('High','Medium','Low', 'Informational')
```


## List all Incidents including types and present severity, time to close, types etc.


## Source: https://secbyte.in/2024/08/18/mastering-sentinel-the-essential-kql-query-for-every-soc-team/<

```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| extend ProductName = tostring(parse_json(tostring(AdditionalData.alertProductNames))[0])
| summarize arg_max(TimeGenerated, *) by IncidentNumber
| extend IncidentDuration = iif(Status == "Closed", datetime_diff('minute', ClosedTime, CreatedTime), datetime_diff('minute', now(), CreatedTime))
| summarize IncidentCount = count()
    by
    IncidentNumber,
    tostring(AlertIds),
    TimeGenerated,
    Title,
    Severity,
    Status,
    IncidentDuration,
    ProviderName,
    ProductName
| extend Alerts = extract("\\[(.*?)\\]", 1, tostring(AlertIds))
| mv-expand todynamic(AlertIds) to typeof(string)
| join (
    SecurityAlert
    | summarize AlertCount = count() by AlertSeverity, SystemAlertId, AlertName, Status
    )
    on $left.AlertIds == $right.SystemAlertId
| summarize Alert_Count=sum(AlertCount), make_set(AlertName)
    by
    IncidentNumber,
    Title,
    Severity,
    Status,
    IncidentDuration,
    ProviderName,
    TimeGenerated,
    ProductName
| extend ["Alert Name"] = tostring(set_AlertName[0])
| summarize
    TotalIncidents = count(),
    FirstIncidentTime= min(TimeGenerated),
    LastIncidentTime=max(TimeGenerated),
    ClosedIncidents = countif(Status == "Closed"),
    ActiveIncidents = countif(Status == "Active"),
    NewIncidents = countif(Status == "New"),
    AvgIncidentDuration = avg(IncidentDuration),
    MaxIncidentDuration = max(IncidentDuration),
    MinIncidentDuration = min(IncidentDuration),
    SeverityDistribution = make_list(Severity)
    by ProviderName, Title, ProductName
| project
    FirstIncidentTime,
    LastIncidentTime,
    ProviderName,
    ProductName,
    Title,
    TotalIncidents,
    ClosedIncidents,
    ClosedPercentage=strcat(round(ClosedIncidents * 100.0 / TotalIncidents, 1), "%"),
    ActiveIncidents,
    ActivePercentage=strcat(round(ActiveIncidents * 100.0 / TotalIncidents, 1), "%"),
    NewIncidents,
    NewPercentage=strcat(round(NewIncidents * 100.0 / TotalIncidents, 1), "%"),
    round(AvgIncidentDuration, 2),
    MaxIncidentDuration,
    MinIncidentDuration,
    SeverityDistribution
| sort by TotalIncidents desc
```
