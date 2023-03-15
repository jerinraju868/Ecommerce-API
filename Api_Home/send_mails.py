import smtplib
from email.mime.text import MIMEText
from socket import gaierror

try:
    email_from = 'jerin@gmail.com'
    email_to = 'jerin@gmail.com'
    email_subject = 'Checkout mail'
    email_body = ''
    message = MIMEText(email_body)
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = email_subject
    smtp_server = 'smtp.mailtrap.io'
    smpt_port = 465
    smtp_username = 'c9afbb9b64a4fe'
    smtp_password = '99d9eb81e7a8ee'
    server = smtplib.SMTP(smtp_server, smpt_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email_from, email_to, message.as_string())
    server.quit()
    print('Mail send successfully..')
except (gaierror, ConnectionRefusedError):
    print('\n Failed to connect to the server. Check your internet connection.\n')
except smtplib.SMTPServerDisconnected as s:
    print('\nInvalid credentials...!\n',s)
except Exception as e:
    print('\nSomething went wrong...!\n',e)