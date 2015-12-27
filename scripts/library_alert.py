# -*- coding: utf-8 -*-
# @Date    : 2015-12-16 19:40:33
# @Author  : Lucien Zhou 
import re
import datetime
import requests
from bs4 import BeautifulSoup
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def get_dates():
    url = 'https://ftp.lib.hust.edu.cn/patroninfo*chx'
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }

    form_data = {'name':'###',
                 'code':'###',
                 'submit.x':'35',
                 'submit.y':'19',
                 'submit':'submit'}
    s = requests.session()
    response = s.post(url, data = form_data, headers = header)

    soup = BeautifulSoup(response.content)

    dates = soup.find_all("td",{"class":"patFuncStatus"})
    return dates

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_alert_email():
    from_addr = '###@gmail.com'
    password = '###'
    to_addr = '###@qq.com'

    msg = MIMEText('同学，您在图书馆借的书籍已到期，请赶紧缴费归还\n\
        本邮件由Python爱好者发送，保证并没有在浏览器查看您的借阅记录，书籍到期检测和邮件发送均由程序自动实现\n\
        此次邮件发送仅为测试所用，不会侵犯您的隐私，如您以后还需要自动提醒服务，请联系###。很抱歉打扰到您。', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'python<%s>' % from_addr)
    msg['To'] = _format_addr(u'self <%s>' % to_addr)
    msg['Subject'] = Header(u'图书馆', 'utf-8').encode()

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def get_Due_date(dates):
    regex = r'(\d\d-\d\d-\d\d)'
    date_list = []
    pattern = re.compile(regex)
    for date in dates:
        date_list.append(date.text)
    Due_date_list = re.findall(pattern,str(date_list))
    return Due_date_list


dates = get_dates()
if dates:
    Due_date_list = get_Due_date(dates)
for date_string in Due_date_list:
    year = '20'+ date_string[0:2]
    month = date_string[3:5].lstrip('0')
    day = date_string[-2:].lstrip('0')
    Due_date = datetime.date(int(year),int(month),int(day))
    today = datetime.date.today()
    timedelta = Due_date - today
    if timedelta.days< 7:
        send_alert_email()
        break
