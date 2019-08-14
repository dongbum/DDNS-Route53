# -*- coding: utf-8 -*-

import configparser

class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.domain = config['DEFAULT']['DOMAIN']
        self.aws_hosted_zone_id = config['DEFAULT']['AWS_HOSTED_ZONE_ID']
        self.aws_access_key_id = config['DEFAULT']['AWS_ACCESS_KEY_ID']
        self.aws_secret_access_key = config['DEFAULT']['AWS_ACCESS_SECRET_KEY']
