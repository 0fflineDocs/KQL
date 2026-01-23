# FileAttachment Name


## Hunt for emails with attachment name patterns (QR Code)

```kql
EmailAttachmentInfo | 
where FileType in ("png", "jpg", "jpeg", "gif", "svg")  | 
where isnotempty(FileName) | 
extend firstFourFileName = substring(FileName, 0, 4)  | 
summarize RecipientsCount = dcount(RecipientEmailAddress), FirstFourFilesCount = dcount(firstFourFileName), suspiciousEmails = make_set(NetworkMessageId, 10) by SenderFromAddress | 
where FirstFourFilesCount >= 10 
```
