import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Victoria'
email['to'] =
email['subject'] = 'Email sender test'

email.set_content(html.substitute(name='Andy'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login()
    smtp.send_message(email)
    print('email sent!')