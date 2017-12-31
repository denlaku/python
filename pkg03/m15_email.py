# coding=UTF-8
# pylint: disable=invalid-name
'''
email
'''
import email
# from email import mime
from email.mime import (multipart, text)
import smtplib
print(email.__all__)

msg = multipart.MIMEMultipart()
msg['from'] = 'ustchacker@tom.com'
msg['to'] = 'blablabla@aliyun.com'
msg['subject'] = 'test'
content = '''
Hello World
'''

txt = text.MIMEText(content)
msg.attach(txt)
smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login('1274409336@qq.com', 'tl250026')
smtp.sendmail('1274409336@qq.com', '1274409336@qq.com', str(msg))
smtp.quit()



print("-----------------------------")
