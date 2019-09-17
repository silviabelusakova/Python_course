#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEText('This is test mail')  #MIMEText std format pre odoslanie textu spravy na rozdiel od jednoducheho text stringu (co moze generovat chyby)


msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = 'b09a2e8c12abe3'
password = '250b340958a9b5'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")