
# Flask-Mail
Flask-Mail 扩展提供了一个简单的发送邮件的接口，可以在 Flask 应用中设置 SMTP 来完成发送邮件信息的功能。

# 开启smtp服务
这里利用的qq邮箱的SMTP服务，所以首先需要先开启该服务并获得授权码。在qq邮箱“**邮箱设置 — 账户 — POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务**”里找到下图位置，开启SMTP服务。
```text
POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务
----------------------------------------------
开启服务：
    POP3/SMTP服务 (如何使用 Foxmail 等软件收发邮件？) 		已开启 |  关闭
    IMAP/SMTP服务 (什么是 IMAP，它又是如何设置？) 			已开启 |  关闭
    Exchange服务 (什么是Exchange，它又是如何设置？) 			已关闭 |  开启
    CardDAV/CalDAV服务 (什么是CardDAV/CalDAV，它又是如何设置？) 已关闭 |  开启
    (POP3/IMAP/SMTP/CardDAV/CalDAV服务均支持SSL连接。如何设置？)
```
可能会提示发送短信进行验证，发送完后会提供一个16位的授权码，这个需要保存后续发送邮箱时密码就填这个授权码。

# 安装 Flask-Mail
```shell
	pip install Flask-Mail
```

# Flask-Mail配置说明
```text
配置项					  默认值			 功能
MAIL_SERVER				localhost		邮箱服务器
MAIL_PORT				25				端口
MAIL_USE_TLS			False			是否使用TLS
MAIL_USE_SSL			False			是否使用SSL
MAIL_DEBUG				app.debug		是否为DEBUG模式，打印调试消息
MAIL_SUPPRESS_SEND		app.testing		设置是否真的发送邮件，True不发送
MAIL_USERNAME			None			用户名，填邮箱
MAIL_PASSWORD			None			密码，填授权码
MAIL_DEFAULT_SENDER		None			默认发送者，填邮箱
MAIL_MAX_EMAILS			None			一次连接中的发送邮件的上限
MAIL_ASCII_ATTACHMENTS	False			如果 MAIL_ASCII_ATTACHMENTS 设置成 True 的话，文件名将会转换成 ASCII 的。一般用于添加附件。
```

参考:
1. [Flask 邮件](https://www.w3cschool.cn/flask/flask_mail.html)
2. [使用Flask-Mail和qq邮箱SMTP服务发送邮件](https://blog.csdn.net/wbin233/article/details/73222027)