# -*- coding: utf-8 -*-

import os, configparser
from ddns.customerror import ConfigParserError

class Config:
    def __init__(self):
        try:
            if os.path.exists('config.ini'):
                config = configparser.ConfigParser()
                config.read('config.ini')
                self.domain = config['DEFAULT']['DOMAIN']
                self.aws_hosted_zone_id = config['DEFAULT']['AWS_HOSTED_ZONE_ID']
                self.aws_access_key_id = config['DEFAULT']['AWS_ACCESS_KEY_ID']
                self.aws_secret_access_key = config['DEFAULT']['AWS_ACCESS_SECRET_KEY']
                self.get_ip = config['DEFAULT']['GET_IP']
                self.check_url = config['DEFAULT']['CHECK_URL']
                self.log = config['DEFAULT']['LOG']
            else:
                self.domain = os.environ['DOMAIN']
                self.aws_hosted_zone_id = os.environ['AWS_HOSTED_ZONE_ID']
                self.aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
                self.aws_secret_access_key = os.environ['AWS_ACCESS_SECRET_KEY']
                self.get_ip = os.environ['GET_IP']
                self.check_url = os.environ['CHECK_URL']
                self.log = os.environ['LOG']
        except:
            raise ConfigParserError('Load config failed.')
