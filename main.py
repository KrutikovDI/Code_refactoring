import email
import smtplib
import imaplib
from typing import Self
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"



class MailWork:
    def __init__(self, path, recipients, subject, message, passwORD):
#send message
        self.msg = MIMEMultipart()
        self.msg['From'] = path
        self.msg['To'] = ', '.join(recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message))


        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(path, passwORD)
        ms.sendmail(path, ms, self.msg.as_string())

        ms.quit()
#send end


#recieve
    def MailRecieve(header = None):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(path, passwORD)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result_data = mail.uid('search', None, criterion)
        assert result_data[0], 'There are no letters with current header'
        latest_email_uid = result_data[0].split()[-1]
        result_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = result_data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
#end recieve

if __name__ == '__main__':
    path = 'login@gmail.com'
    passwORD = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    exampl = MailWork(path, recipients, subject, message, passwORD)
    exampl.MailRecieve()