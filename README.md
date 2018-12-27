# Emailer

This project is an email birth announcement that can be sent to all your family & friends when your bundle of joy arrives. Initially, it was created to send via text, but due to applicable charges from mobile carriers, that idea got scrapped. Instead, you can email everyone with a click of a button.

## Getting Started

You need Python3 in your system to use this module.

### Example Usage of the Module

```
from Emailer import Emailer

sendersEmail = "sender@gmail.com" #Sender's Email Address
sendersPassword = "sender@123456" #Sender's Password
recipients = ["user_name1@gmail.com","user_name2@gmail.com","user_name3@gmail.com"]
subject = "Informing about ..."
body = "Hello everyone, I hope you all are in good health..."

Emailer.send_email(sendersEmail,sendersPassword,recipients,subject,body)
``` 

### Using defualt birth announcement message function

```
sendersEmail = "sendersEmailAddress"
sendersPassword = "sendersPassword"
recipients = ["user_name1@gmail.com","user_name2@gmail.com","user_name3@gmail.com"]
childName = "Emma Smith"
date = "January 15, 2016"
time = "11:00 AM"
weight = "8 pounds, 7 ounce"
height = "11 inches"

Emailer.send_birth_email(senderEmail,sendersPassoword,recipients,childName,date,time,weight,height)
```  

### Solving Gmail Authentication Error
Follow this link https://devanswers.co/allow-less-secure-apps-access-gmail-account/


