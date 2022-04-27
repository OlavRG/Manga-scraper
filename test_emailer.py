# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:47:20 2022

@author: olavg

Email might start failing after May30th when google stops allowing 3rd party apps
Current protection for email:
    two step authentication
    application password (https://support.google.com/accounts/answer/185833?hl=en#zippy=)

                          
"""

import smtplib
import ssl

SERVER_ADDRESS = 'smtp.gmail.com'
SERVER_PORT = 587
EMAIL_ADDRESS = 'autoolav0@gmail.com'
EMAIL_PASSWORD = 'hwpycfztjrvbjrpg' #'DvfAD95P!7PC'
RECIPIENT_EMAIL = 'olavgrouwstra@gmail.com'

context = ssl.create_default_context()

with smtplib.SMTP(SERVER_ADDRESS, SERVER_PORT) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, 'Hello World')
