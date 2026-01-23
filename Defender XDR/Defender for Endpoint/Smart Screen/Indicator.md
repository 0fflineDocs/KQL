# Indicator


## MDE Indicator Warn + MDA Monitored App

```kql
DeviceEvents
| where Timestamp > ago(7d)
| where ActionType in ("SmartScreenUserOverride", "NetworkProtectionUserBypassEvent")
| extend Browser = case(
        InitiatingProcessFileName has "msedge", "Edge",
        InitiatingProcessFileName has "chrome", "Chrome", 
        InitiatingProcessFileName has "firefox", "Firefox",
        InitiatingProcessFileName has "opera", "Opera",
"3rd party browser")
| project Timestamp, DeviceId, DeviceName, ActionType, Browser, RemoteUrl
```
