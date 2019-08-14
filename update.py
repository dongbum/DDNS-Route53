# -*- coding: utf-8 -*-

from ddns.iputils import IPUtils
from ddns.recordfile import RecordFile
from ddns.awscommand import AWSCommand
from ddns.customerror import *

try:
    current_ip = IPUtils.getrealip()

    # old_ip = RecordFile.get_old_ip(current_ip)  # 예전 IP를 가져온다.
    old_ip = AWSCommand.get_ip()

    print('Old:[%s] Current:[%s]' % (old_ip, current_ip)) # 실제 아이피를 가져올 수 있다.

    if str(old_ip) == str(current_ip):
        print('same')
    else:
        print('not same')
        AWSCommand.update_ip(current_ip)

except Exception as e:
    print(e)
    exit(-1)
