# SuspiciousEmail ClickOnURL


## Users who received suspicious emails and clicked on URL's

```kql
let UserClickedLink = (UrlClickEvents 
| where Workload == "Email"
| where ActionType == "ClickAllowed" or IsClickedThrough != "0");
EmailEvents
| where EmailDirection == "Inbound"
| where ThreatTypes has_any ("Phish", "Malware")
| join kind = inner UserClickedLink on NetworkMessageId
| project Timestamp, ReportId, NetworkMessageId, SenderFromAddress, RecipientEmailAddress, ActionType, IsClickedThrough, Url 
```
