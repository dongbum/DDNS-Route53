# -*- coding: utf-8 -*-

import boto3

class AWSCommand:
    @staticmethod
    def update_ip(current_ip):
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