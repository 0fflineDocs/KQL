## KQL_Cheat_Sheet

### Defender ATP

#### TVM Vulnerabilites

###### (critical 1days) 
**let newVuln = DeviceTvmSoftwareVulnerabilitiesKB**  
| where VulnerabilitySeverityLevel == "Critical"  
| where LastModifiedTime >ago(1day); DeviceTvmSoftwareInventoryVulnerabilities   
| join newVuln on CveId  
| summarize dcount(DeviceId) by DeviceName, DeviceId, Timestamp=LastModifiedTime, SoftwareName, SoftwareVendor, SoftwareVersion, VulnerabilitySeverityLevel, CvssScore, IsExploitAvailable  
| project Timestamp, DeviceName, SoftwareName, SoftwareVendor, SoftwareVersion, VulnerabilitySeverityLevel, CvssScore, IsExploitAvailable, DeviceId

###### URL: https://github.com/jangeisbauer/AdvancedHunting/blob/master/Detected%20new%20Vuln%20in%20Enterprise   
  
**DeviceTvmSoftwareInventoryVulnerabilities**  
| project  DeviceName, SoftwareName, CveId, SoftwareVersion, VulnerabilitySeverityLevel   
| join (DeviceTvmSoftwareVulnerabilitiesKB  
| project AffectedSoftware, VulnerabilityDescription , CveId , CvssScore , IsExploitAvailable) on CveId   
| project CveId , SoftwareName , SoftwareVersion , VulnerabilityDescription , VulnerabilitySeverityLevel, IsExploitAvailable , CvssScore   
| distinct SoftwareName , SoftwareVersion, CveId, VulnerabilityDescription , VulnerabilitySeverityLevel, IsExploitAvailable    
| sort by SoftwareName asc , SoftwareVersion  
____  
#### UEFI SCAN  
###### URL: https://www.microsoft.com/security/blog/2020/06/17/uefi-scanner-brings-microsoft-defender-atp-protection-to-a-new-level/

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

_____

#### Controlled Folder Access  
**DeviceEvents**  
| where ActionType in ('ControlledFolderAccessViolationAudited','ControlledFolderAccessViolationBlocked')

#### Exploit Protection / Network Protection  
**DeviceEvents**  
| where ActionType startswith 'ExploitGuard' and ActionType !contains 'NetworkProtection'

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
