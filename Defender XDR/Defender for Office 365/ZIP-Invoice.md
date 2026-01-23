# ZIP Invoice


## Hunt all emails with ZIP attachments received from the same list of TLDs as identified malicious email

```kql
EmailAttachmentInfo
| where Timestamp > ago(4h)
| where FileType == "zip"
| where SenderFromAddress has_any (".br", ".ru", ".jp")
```


## Hunt for emails containing zip files based on the name invoice, extract hash and filename (add to tenant block list)

```kql
EmailAttachmentInfo
| where Timestamp > ago(8h)
| where FileType == "zip"
| where FileName contains "invoice"
| distinct SHA256, FileName
```
