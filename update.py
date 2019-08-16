# -*- coding: utf-8 -*-

from ddns.logmanager import Log
from ddns.iputils import IPUtils
from ddns.recordfile import RecordFile
from ddns.awscommand import AWSCommand
from ddns.config import Config

try:
    log = Log()
    current_ip = IPUtils.getrealip()

    config = Config()
    if str(config.get_ip).upper() == 'FILE':
        old_ip = RecordFile.get_old_ip(current_ip)  # 예전 IP를 가져온다.
    elif str(config.get_ip).upper() == 'AWS':
        old_ip = AWSCommand.get_ip()
    else:
        raise Exception('Cannot found IP get method.')

    Log.write('Old:[%s] Current:[%s]' % (old_ip, current_ip)) # 실제 아이피를 가져올 수 있다.

    if str(old_ip) == str(current_ip):
        Log.write('IP not changed.')
    else:
        Log.write('IP change detected.')
        AWSCommand.update_ip(current_ip)

except Exception as e:
    Log.write(e)
    exit(-1)
