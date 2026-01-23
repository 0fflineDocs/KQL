# Suspicious MailboxRules


## Check suspicious Mailbox rules

```kql
CloudAppEvents
| where Timestamp between (start .. end) //Timestamp from the app creation time to few hours, usually before spam emails sent
| where AccountObjectId in ("<Impacted AccountObjectId>")
| where Application == "Microsoft Exchange Online"
| where ActionType in ("New-InboxRule", "Set-InboxRule", "Set-Mailbox", "Set-TransportRule", "New-TransportRule", "Enable-InboxRule", "UpdateInboxRules")
| where isnotempty(IPAddress)
| mvexpand ActivityObjects
| extend name = parse_json(ActivityObjects).Name
| extend value = parse_json(ActivityObjects).Value
| where name == "Name"
| extend RuleName = value 
| project Timestamp, ReportId, ActionType, AccountObjectId, IPAddress, ISP, RuleName
```
