import sys
import smtplib
import json

def send_email(senderEmail,senderPassword, recipients, subject, body):
    '''
        recipients: a list
        
        Return True if email sent successfully 
    '''
    
    FROM = senderEmail
    TO = recipients
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(senderEmail, senderPassword)
        server.sendmail(FROM, TO, message)
        server.close()
        print('Successfully sent the email')
        return True
    except Exception as e:
        print("Failed to send email",e)
        return False

def send_email_from_input(inputFilePath): 
    '''
        input file should have format as given in README.md 
    '''
    with open(inputFilePath, 'rb') as fp:
        data = json.load(fp)
        return send_email(data['sendersEmail'],
                          data['sendersPassword'],
                          data['recipients'],
                          data['emailSubject'], 
                          data['emailBody'])
    
def send_birth_email(sendersEmail, sendersPassword, recipients, childName, birthDate, birthTime, weight, height):
    emailText = """Dear Family & Friends,\nWell look who decided to drop by . . .%s. Born %s, at %s. %s | %s."""%(childName,birthDate,birthTime,weight,height)
    emailSubject = "Birth Announcement"
    send_email(sendersEmail,sendersPassword,recipients,emailSubject,emailText)    
    
if __name__=="__main__":
    if(len(sys.argv)>1): 
        inputFilePath = sys.argv[1]
    else:
        raise Exception('input file path not found.')
    
    send_email_from_input(inputFilePath)
    
    