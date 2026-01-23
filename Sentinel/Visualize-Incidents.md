# Visualize Incidents


## List all incidents by Severity

```kql
let CollectIncidentSeverity = (TimeSpan: timespan) {
    SecurityIncident
    | where TimeGenerated > ago(TimeSpan)
    | summarize arg_max(TimeGenerated, *) by IncidentNumber
    | summarize TotalIncidents = count() by Severity
    | render piechart 
};
CollectIncidentSeverity(30d)
```


## List all incidents by titles and include count

```kql
let CollectIncidentStatistics = (TimeSpan: timespan) {
    SecurityIncident
    | where TimeGenerated > ago(TimeSpan)
    | summarize arg_max(TimeGenerated, *) by IncidentNumber
    | summarize TotalIncidents = count() by Title
};
CollectIncidentStatistics(30d)
```


## List all incidents by tactic

```kql
let CollectIncidentTactics = (TimeSpan: timespan) {
    SecurityIncident
    | where TimeGenerated > ago(TimeSpan)
    | summarize arg_max(TimeGenerated, *) by IncidentNumber
    | extend TacticsArray = parse_json(AdditionalData).tactics
    | mv-expand Tactic = TacticsArray
    | summarize Total = count() by tostring(Tactic)
    | sort by Total desc
    | render piechart
};
CollectIncidentTactics(30d)
```
