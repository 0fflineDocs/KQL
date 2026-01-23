# WaaS

```kql
Legacy Update Compliance (Azure Marketplace)
```


## Feature Update deployment issues

```kql
WaaSDeploymentStatus | where UpdateCategory == "Feature" | where DeploymentStatus == "Failed" or DeploymentError != ""
```


## Deferral configurations for Feature Update

```kql
WaaSUpdateStatus | summarize count(ComputerID) by FeatureDeferralDays | render columnchart
```


## Pause configurations for Feature Update

```kql
WaaSUpdateStatus | summarize count(ComputerID) by FeaturePauseState | render columnchart
```


## Devices pending reboot to complete feature updates

```kql
WaaSDeploymentStatus | where UpdateCategory == "Feature" | where DetailedStatus in ("Reboot required", "Reboot pending")
```


## Devices with a safeguard hold

```kql
WaaSDeploymentStatus | where DetailedStatus == "Safeguard Hold"
```


## Target build distribution of devices with a safeguard hold

```kql
WaaSDeploymentStatus | where DetailedStatus == "Safeguard Hold" | summarize count(ComputerID) by TargetBuild | render piechart
```


## Security Update Deployment Issues

```kql
WaaSDeploymentStatus | where UpdateCategory == "Quality" | where DeploymentStatus == "Failed" or DeploymentError != ""
```


## Deferral configurations for Quality Update

```kql
WaaSUpdateStatus | summarize count(ComputerID) by QualityDeferralDays | render columnchart
```


## Pause configurations for Quality Update

```kql
WaaSUpdateStatus | summarize count(ComputerID) by QualityPauseState | render columnchart
```


## Devices pending reboot to complete security updates

```kql
WaaSDeploymentStatus | where UpdateCategory == "Quality" | where DetailedStatus in ("Reboot required", "Reboot pending")
```


## OS Edition distribution for the devices

```kql
WaaSUpdateStatus | summarize DeviceCount = count() by OSEdition | render table
```


## Inventory of devices on Insider builds

```kql
WaaSInsiderStatus
```


## Last scan time distribution

```kql
WaaSUpdateStatus | union WaaSInsiderStatus | extend LastSca
```
