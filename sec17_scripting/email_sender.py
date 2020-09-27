import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Dadong Zhang'
email['to'] = 'doubleomics@gmail.com'
email['subject'] = 'Recommandations for python class'

email.set_content('I am learning Python at Udemy and highly recommend it for you!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ddzhangzz@gmail.com', 'Sienna@103')
    smtp.send_message(email)
    print('all good boss~')