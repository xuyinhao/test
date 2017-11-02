import smtplib
from email.mime.text import MIMEText
from email.header import Header

data=open('../../user_passwd','r')
data_line=data.readline()
data.close()

smtpserver=data_line.split(',')[0]
user=data_line.split(',')[1]
password=data_line.split(',')[2]
recer=data_line.split(',')[3]

subject='python email test'
#html 邮件的正文
msg=MIMEText('<html><h1>傻孩子 你好</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

#连接发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtpserver,25)
smtp.login(user,password)
smtp.sendmail(user,recer,msg.as_string())
smtp.quit()