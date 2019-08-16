# -*- coding: utf-8 -*-

from ddns.logmanager import Log
from ddns.iputils import IPUtils
from ddns.recordfile import RecordFile
from ddns.awscommand import AWSCommand
from ddns.customerror import *

try:
    log = Log()
    current_ip = IPUtils.getrealip()

    # old_ip = RecordFile.get_old_ip(current_ip)  # 예전 IP를 가져온다.
    old_ip = AWSCommand.get_ip()

    Log.write('Old:[%s] Current:[%s]' % (old_ip, current_ip)) # 실제 아이피를 가져올 수 있다.

    if str(old_ip) == str(current_ip):
        Log.write('same')
    else:
        Log.write('not same')
        AWSCommand.update_ip(current_ip)

except Exception as e:
    Log.write(e)
    exit(-1)
