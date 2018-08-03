#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
  Created by tao.liu on 2018/8/3.
  description this is description
"""
import smtplib
from email.mime.text import MIMEText


def sendEmail(fromAdd, toAdd, subject, text):
    _pwd = "viuhiqhjacjgdgji"  # 授权码

    msg = MIMEText(text)
    msg["Subject"] = subject
    msg["From"] = fromAdd
    msg["To"] = toAdd
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(fromAdd, _pwd)
        s.sendmail(fromAdd, toAdd, msg.as_string())
        s.quit()
        print("Success!")
    except smtplib.SMTPException:
        print('Falied!')


if __name__ == '__main__':
    from_ = "1937553940@qq.com"  # 你的邮箱   发件地址
    to_ = input('Please input Recipient:')  # 收件地址
    subject = input('Please input title:')  # 邮件标题
    text = input('Please input Content:')  # 邮件内容

    sendEmail(from_, to_, subject, text)
