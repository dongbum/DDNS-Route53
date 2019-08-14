# -*- coding: utf-8 -*-

from ddns.iputils import IPUtils
from ddns.recordfile import RecordFile
from ddns.awscommand import AWSCommand

current_ip = IPUtils.getrealip()
print(current_ip) # 실제 아이피를 가져올 수 있다.

old_ip = RecordFile.get_old_ip(current_ip)  # 예전 IP를 가져온다.

if str(old_ip) == str(current_ip):
    print('same')
else:
    print('not same')

AWSCommand.update_ip(current_ip)