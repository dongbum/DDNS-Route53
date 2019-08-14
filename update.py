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
current_ip = BeautifulSoup(html, "html.parser")

print(str(current_ip)) # 실제 아이피를 가져올 수 있다.

# IP를 저장해놓은 파일을 열어 예전 아이피와 비교한다.
try:
    if os.path.exists('old_ip.txt'):
        f = open('old_ip.txt', mode='rt', encoding='utf-8')
        old_ip = f.read()   # 파일이 이미 존재하면 아이피를 읽어온다.
        f.close()
    else:
        f = open('old_ip.txt', mode='wt', encoding='utf-8')
        f.write(str(current_ip))    # 파일이 존재하지 않는다면 파일을 생성하고 현재 아이피를 추가한다.
        old_ip = str(current_ip)
        f.close()

    print('old_ip : ' + old_ip)
except FileNotFoundError:
    print('file error')

if str(old_ip) == str(current_ip):
    print('same')
else:
    print('not same')

client = boto3.client('route53')
response = client.change_resource_record_sets(
    HostedZoneId='string',
    ChangeBatch={
        'Comment': 'string',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'home.83rpm.com',
                    'Type': 'A',
                    'TTL': 60
                },
                'ResourceRecords': [
                    {
                        'Value': 'IP'
                    }
                ]
            }
        ]
    }
)