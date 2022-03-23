import smtplib
import datetime as dt
import schedule
import time
from email.mime.multipart import *
from email import encoders
from email.mime.text import *
from email.header import Header
from email.utils import *
from email.mime.application import *


def send_email():
    sender = "2018ashley2333@gmail.com"  # 在这里写发件人的邮箱

    receiver = "gavint@diversityarrays.com"  # 在这里写收件人的邮箱

    subject = "report"  # 这里是邮件主题

    from_addr = "2018ashley2333@gmail.com"  # 这里写发件人的邮箱地址

    password = "xgy961205"

    msg = MIMEMultipart()

    msg['Subject'] = subject

    msg['to'] = receiver

    msg['from'] = "Ashley Xiao"  # 你的名字

    body = ""  # 这里是正文

    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    xlsxpart = MIMEApplication(open('Report.pdf', 'rb').read())  # 附件的地址
    xlsxpart.add_header('Content-Disposition', 'attachment', filename='Report.pdf')  # 这里是附件最后发过去的名字
    msg.attach(xlsxpart)

    smtp_server = "smtp.gmail.com"  # 你用什么邮箱就写什么邮箱的smtp地址我这里只是个例子。
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)

    server.ehlo()
    server.starttls()
    server.login(from_addr, password)

    server.sendmail(from_addr, receiver.split(','), msg.as_string())

    server.quit()


schedule.every().monday.at("06:30").do(send_email)
while True:
    schedule.run_pending()
    time.sleep(60)
