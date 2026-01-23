# DetectURLWarnings


## Detect Smart Screen URL Warnings

```kql
 let minTimeRange = ago(7d);
 DeviceEvents
    | where ActionType == "SmartScreenUrlWarning" and Timestamp > minTimeRange
```


## Filter out SmartScreen test URLs under https://demo.smartscreen.msft.net/

```kql

            and RemoteUrl !startswith "https://demo.smartscreen.msft.net/" 
    | extend ParsedFields=parse_json(AdditionalFields)
    | project Timestamp, DeviceName, BlockedUrl=RemoteUrl, Recommendation=tostring(ParsedFields.Recommendation), Experience=tostring(ParsedFields.Experience), ActivityId=tostring(ParsedFields.ActivityId); 
```
