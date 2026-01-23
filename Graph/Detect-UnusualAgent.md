# Detect UnusualAgent


## Detect Unusual Agent - https://cloudbrothers.info/en/detect-threats-microsoft-graph-logs-part-2/

```kql
let HistoricalActivity = MicrosoftGraphActivityLogs
    | where TimeGenerated between (ago(30d) .. startofday(now()))
    | where isnotempty(UserAgent)
    | extend ObjectId = iff(isempty(UserId), ServicePrincipalId, UserId)
    | extend ObjectType = iff(isempty(UserId), "ServicePrincipalId", "UserId")
    | summarize by ObjectId, UserAgent, IPAddress;
MicrosoftGraphActivityLogs
| where TimeGenerated between (startofday(now()) .. now())
| extend ObjectId = iff(isempty(UserId), ServicePrincipalId, UserId)
| where isnotempty(UserAgent)
```


## Remove known user agents

```kql
| join kind=leftanti (HistoricalActivity
    | summarize by ObjectId, UserAgent
    )
    on UserAgent, ObjectId
```


## Remove known IP addresses to limit false positives


## | join kind=leftanti (HistoricalActivity | summarize by IPAddress) on IPAddress
