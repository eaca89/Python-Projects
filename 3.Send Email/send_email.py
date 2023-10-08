import smtplib
import ssl
from getpass import getpass

smtp_server = 'smtp.gmail.com'
port = 465

sender_email = 'someemail@gmail.com'  # make sure to change this sample email
password = getpass(prompt='Enter your password:')
receiver_email = 'test@test.com'  # make sure to change this sample email

message = '''\
Subject: Test

This message is from me.
'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
