# -*- coding: utf-8 -*-

import os
import boto3
import socket
import urllib
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# print(socket.gethostbyname(socket.gethostname()))
# print(socket.gethostbyname_ex(socket.gethostname()))
# print(socket.gethostbyname(socket.getfqdn()))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com", 80))
r = s.getsockname()[0]
s.close()
# print(r)

html = urlopen("http://bot.whatismyipaddress.com")
result = BeautifulSoup(html, "html.parser")

print(str(result)) # 실제 아이피를 가져올 수 있다.

client = boto3.client('route53')

try:
    if os.path.exists('old_ip.txt'):
        f = open('old_ip.txt', mode='rt', encoding='utf-8')
        old_ip = f.read()
        print('old_ip : ' + old_ip)
        f.close()
    else:
        print('file not found')

except FileNotFoundError:
    print('file error')