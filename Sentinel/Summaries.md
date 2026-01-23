# Summaries


## Severity

```kql
SecurityAlert
| summarize count() by Severity
| render piechart 
```


## Products

```kql
SecurityAlert
| summarize count() by ProductName
| render piechart 
```


## Tactics

```kql
SecurityAlert
| summarize count() by Tactics
| render piechart 
```
