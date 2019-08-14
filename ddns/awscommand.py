# -*- coding: utf-8 -*-

import boto3
from ddns.config import Config

class AWSCommand:
    @staticmethod
    def update_ip(current_ip):
        config = Config()
        domain = config.domain
        aws_hosted_zone_id = config.aws_hosted_zone_id
        aws_access_key_id = config.aws_access_key_id
        aws_access_secret_key = config.aws_secret_access_key

        client = boto3.client('route53',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_access_secret_key)

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

    @staticmethod
    def get_ip():
        config = Config()
        domain = config.domain
        aws_hosted_zone_id = config.aws_hosted_zone_id
        aws_access_key_id = config.aws_access_key_id
        aws_access_secret_key = config.aws_secret_access_key

        client = boto3.client('route53',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_access_secret_key)

        response = client.list_resource_record_sets(
            HostedZoneId=aws_hosted_zone_id,
            StartRecordName=domain,
            StartRecordType='A'
        )

        # print(response['ResourceRecordSets'])

        for resource in response['ResourceRecordSets']:
            # print(str(resource['Name']) + ' : ' + str(domain))
            if str(domain) in str(resource['Name']):
                return str(resource['ResourceRecords'][0]['Value'])
