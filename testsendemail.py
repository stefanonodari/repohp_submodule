# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import smtplib
from email.mime.text import MIMEText
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
subject = "Email Subject"
body = "terzo commit  This is the body of the text message"
sender = "testdevopsnodari@gmail.com"
recipients = ["snodari@yahoo.com"]
password = "rbvgxwmqicsatzrp"
send_email(subject, body, sender, recipients, password)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
