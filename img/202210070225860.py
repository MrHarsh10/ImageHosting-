import time
import requests
from lxml import etree
import random
import os



header={
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "95",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "PHPSESSID=7mgknu1vmb8j67f891tvnr8uqp; 7649e4d93e96c457af4e1ec56cf9e064__typecho_first_run=1; 7649e4d93e96c457af4e1ec56cf9e064__viewsCounter=16",
    "Host": "bananapool.top",
    "Origin": "http://bananapool.top",
    "Referer": "http://bananapool.top/index.php/archives/16/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34",
    "X-Requested-With": "XMLHttpRequest"
}
url ="http://bananapool.top/index.php/archives/16/comment"
for i in range(4000):
    NAME = "Joker" + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
    MAIL = str(random.randint(100, 999)) + str(random.randint(1000, 9999)) + "@" + str(random.randint(10, 99)) + ".com"
    data = {
        "author": NAME,
        "mail": MAIL,
        "url": "https://www.yixiaoxi.com/",
        "text": "Why so serious",
        "_": "791e751415a63f2549b8d5e4b542a90c"
    }
    se = requests.session()
    print(i,NAME)
    r = requests.post(url=url, data=data, headers=header)
    time.sleep(5)
os.remove('2.py')


