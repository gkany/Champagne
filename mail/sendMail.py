# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from threading import Thread
import time 

app = Flask(__name__)
app.config['MAIL_DEBUG'] = True             # 开启debug，便于调试看信息
app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
app.config['MAIL_SERVER'] = 'smtp.qq.com'   # 邮箱服务器
app.config['MAIL_PORT'] = 465               # 端口
app.config['MAIL_USE_SSL'] = True           # 重要，qq邮箱需要使用SSL
app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
app.config['MAIL_USERNAME'] = 'xxx@qq.com'  # 填邮箱
app.config['MAIL_PASSWORD'] = 'AAAABBBBCCCCDDDD'      # 填授权码
app.config['MAIL_DEFAULT_SENDER'] = 'xxx@qq.com'  # 填邮箱，默认发送者
manager = Manager(app)
mail = Mail(app)


# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/')
def index():
    msg = Message(subject='test',
                  sender="xxx@qq.com",  # 需要使用默认发送者则不用填
                  recipients=['xxx@163.com', 'xxx@qq.com'])

    # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
    msg.body = 'sended by flask-email'
    now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    context = '{} {}'.format(msg.body, now)
    msg.html = '<b> {} <b>'.format(context)
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return '<h1>mail send success {}</h1>'.format(now)


if __name__ == '__main__':
    manager.run()

'''
# usage: sendMail.py [-?] {shell,runserver} ...
# python .\sendMail.py runserver
# http://127.0.0.1:5000


PS C:\Users\xxx\Desktop\mail> python .\sendMail.py
usage: sendMail.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help         show this help message and exit

PS C:\Users\xxx\Desktop\mail> python .\sendMail.py runserver
 * Serving Flask app "sendMail" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Jan/2020 15:34:17] "GET / HTTP/1.1" 200 -
send: 'ehlo [10.0.75.1]\r\n'

......

'''
