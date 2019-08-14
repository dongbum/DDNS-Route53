# -*- coding: utf-8 -*-

import boto3
from ddns.config import Config

class AWSCommand:
    @staticmethod
    def update_ip(domain, current_ip):
        config = Config()
        domain = config.get_domain()
        aws_hosted_zone_id = config.get_aws_hosted_zone_id()

        client = boto3.client('route53')
        response = client.change_resource_record_sets(
            HostedZoneId=aws_hosted_zone_id,
            ChangeBatch={
                'Comment': 'string',
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': domain,
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