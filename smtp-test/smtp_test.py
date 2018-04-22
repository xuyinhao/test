import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

data=open('../../user_passwd','r')
data_line=data.readline()
data.close()

smtpserver=data_line.split(',')[0]
user=data_line.split(',')[1]
password=data_line.split(',')[2]
recer=data_line.split(',')[3]


#html 邮件的正文
mail_msg="""
<h1>傻孩子 你好</h1>
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个baidu链接</a></p>
"""
#msg=MIMEText(mail_msg,'html','utf-8')
msg=MIMEMultipart()
msg['From'] = Header("yinhaoxu@hotmail.com", 'utf-8')
msg['To'] =  Header("测试", 'utf-8')
subject='python email test'
msg['Subject'] = Header(subject,'utf-8')
#邮件正文
msg.attach(MIMEText(mail_msg,'html','utf-8'))
#附件构造
att1=MIMEText(open('jiuyou1.1.zip','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octest-stream'
#这里的filename随便写，写什么邮件中就是啥
att1['Content-Disposition']='attachment;filename="jiuyou1.1.zip"'
msg.attach(att1)
#连接发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtpserver,25)
smtp.login(user,password)
smtp.sendmail(user,recer,msg.as_string())
smtp.quit()
