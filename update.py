# -*- coding: utf-8 -*-

import boto3

from ddns.iputils import IPUtils
from ddns.recordfile import RecordFile

current_ip = IPUtils.getrealip()
print(current_ip) # 실제 아이피를 가져올 수 있다.

old_ip = RecordFile.get_old_ip(current_ip)  # 예전 IP를 가져온다.

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
                    'TTL': 60,
                    'ResourceRecords': [
                        {
                            'Value': current_ip
                        }
                    ]
                }
            }
        ]
    }
)