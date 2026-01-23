# ExternalUSBCopy


## List files copied to USB external drives with USB drive information based on FileCreated events associated with most recent USBDriveMount events before file creations.

```kql
let UsbDriveMount = DeviceEvents
| where ActionType=="UsbDriveMounted"
| extend ParsedFields=parse_json(AdditionalFields)
| project DeviceId, DeviceName, DriveLetter=ParsedFields.DriveLetter, MountTime=Timestamp,
ProductName=ParsedFields.ProductName,SerialNumber=ParsedFields.SerialNumber,Manufacturer=ParsedFields.Manufacturer
| order by DeviceId asc, MountTime desc;
let FileCreation = DeviceFileEvents
| where InitiatingProcessAccountName != "system"
| where ActionType == "FileCreated"
| where FolderPath !startswith "C:\\"
| where FolderPath !startswith "\\"
| project ReportId,DeviceId,InitiatingProcessAccountDomain,
InitiatingProcessAccountName,InitiatingProcessAccountUpn,
FileName, FolderPath, SHA256, Timestamp, SensitivityLabel, IsAzureInfoProtectionApplied
| order by DeviceId asc, Timestamp desc;
FileCreation | lookup kind=inner (UsbDriveMount) on DeviceId
| where FolderPath startswith DriveLetter
| where Timestamp >= MountTime
| partition by ReportId ( top 1 by MountTime )
| order by DeviceId asc, Timestamp desc
```
