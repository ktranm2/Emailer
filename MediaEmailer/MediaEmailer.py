import os
from os.path import basename
from os.path import basename
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import smtplib

#Directory to put attachments to be sent in email
attachmentDir = "Attachments"

def send_email_with_attachments(senderEmail,senderPassword, recipients, subject, text, files=[]):
    FROM = senderEmail
    TO = recipients
    
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        with open(f, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(basename(f)))
        msg.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(senderEmail, senderPassword)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print('Successfully sent the email')
        return True
    except Exception as e:
        print("Failed to send email",e)
        return False


def send_birth_email_with_attachments(sendersEmail, sendersPassword, recipients, childName, birthDate, birthTime, weight, height):
    '''
        :sends birth email with child details and take attachments from Attachments folder
        :put attachments to be sent in Attachment folder
        :returns True if sent successfully
    '''
    
    emailSubject = "Birth Announcement"
    emailText = """Dear Family & Friends,\nWell look who decided to drop by . . .%s. Born %s, at %s. %s | %s."""%(childName,birthDate,birthTime,weight,height)
    
    return send_email_with_attachments(sendersEmail,
                                sendersPassword,
                                recipients,
                                emailSubject,
                                emailText,
                                [os.path.join(attachmentDir, f) for f  in os.listdir(attachmentDir)])


#helper method to create attachments directory
def clear_attachments_directory():
    import glob
    files = glob.glob(os.path.join(attachmentDir,"*"))
    for f in files:
        os.remove(f)
    
    