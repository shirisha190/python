#!/usr/bin/env python3
import smtplib
import os
from email.message import EmailMessage

msg = EmailMessage()
msg['subject'] = 'python test 2 '
msg['From'] = ''
msg['To'] = ''
msg.set_content('this is a python test 2')

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()

    smtp.login('','')

#    subject = 'python test email'
#    body = 'Python test email -- for tesing'

#    msg = f"Subject: {subject}\n\n{body}"

#    smtp.sendmail('', '' , msg)
    smtp.send_message(msg)

#jaiaplgmail.com
#tovabbfzzopiggljjaipal123
#http://www.cyberkeeda.com/2020/06/python-send-html-table-as-email-body.html

