# DetectAppBlocks


## Detect Smart Screen App Blocks

```kql
let minTimeRange = ago(7d);
DeviceEvents
    | where ActionType == "SmartScreenAppWarning" and Timestamp > minTimeRange
```


## Filter out SmartScreen test files downloaded from https://demo.smartscreen.msft.net/

```kql

            and not (FileName startswith "knownmalicious" and FileName endswith ".exe")
    | extend ParsedFields=parse_json(AdditionalFields)
    | project Timestamp, DeviceName, BlockedFileName=FileName, SHA1, Experience=tostring(ParsedFields.Experience), ActivityId=tostring(ParsedFields.ActivityId), InitiatingProcessFileName;
```
