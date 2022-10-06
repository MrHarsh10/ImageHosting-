import time
import requests
from lxml import etree
import random
import os



header={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Content-Length": "45",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "PHPSESSID=7mgknu1vmb8j67f891tvnr8uqp;",
"Host": "bananapool.top",
"Origin": "http://bananapool.top",
"Referer": "http://bananapool.top/admin/register.php",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"
}
url ="http://bananapool.top/index.php/action/register?_=4794cd95a568463190b52289a2969604"
for i in range(5000):
    NAME="joker"+str(random.randint(1000,9999))+str(random.randint(0,1234))
    MAIL=NAME+"@"+str(random.randint(100,999))+str(".top")
    data = {
        "name": NAME,
        "mail": MAIL
    }
    r = requests.post(url=url, data=data, headers=header)
    print(i,NAME,MAIL)
    time.sleep(10)