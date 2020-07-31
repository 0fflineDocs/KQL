## KQL_Cheat_Sheet

### Defender ATP

#### UEFI SCAN  
URL: https://www.microsoft.com/security/blog/2020/06/17/uefi-scanner-brings-microsoft-defender-atp-protection-to-a-new-level/

**DeviceEvents**
| where ActionType == "AntivirusDetection"  
| extend ParsedFields=parse_json(AdditionalFields)  
| extend ThreatName=tostring(ParsedFields.ThreatName)  
| where ThreatName contains_cs "UEFI"  
| project ThreatName=tostring(ParsedFields.ThreatName), FileName, SHA1, DeviceName, Timestamp  
| limit 100  

**DeviceAlertEvents**
| where Title has "UEFI"  
| summarize Titles=makeset(Title) by DeviceName, DeviceId, bin(Timestamp, 1d)  
| limit 100  

____  
### Azure AD

#### Conditional Access
  
*Changes to a conditional access-policy and by who*

**AuditLogs**
| where Category == "Policy"  
| project  ActivityDateTime, ActivityDisplayName, TargetResources[0].displayName, InitiatedBy.user.userPrincipalName  

**SigninLogs**
| where ConditionalAccessStatus == "success"  
| project AppDisplayName, Identity, ConditionalAccessStatus    
