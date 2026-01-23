# Malicious URL


## Hunt for malicious URLs and add as indicators in MDE (to block using Network Protection)

```kql
EmailUrlInfo
| where Timestamp > ago(4h)
| where Url contains "malicious.example"
| distinct Url
```
