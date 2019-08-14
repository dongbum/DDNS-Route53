# -*- coding: utf-8 -*-

import configparser

class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.domain = config['DEFAULT']['DOMAIN']
        self.aws_hosted_zone_id = config['DEFAULT']['AWS_HOSTED_ZONE_ID']

    def get_domain(self):
        return self.domain

    def get_aws_hosted_zone_id(self):
        return self.aws_hosted_zone_id