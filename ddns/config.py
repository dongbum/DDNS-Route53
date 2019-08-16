# -*- coding: utf-8 -*-

import configparser
from ddns.customerror import ConfigParserError

class Config:
    def __init__(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.domain = config['DEFAULT']['DOMAIN']
            self.aws_hosted_zone_id = config['DEFAULT']['AWS_HOSTED_ZONE_ID']
            self.aws_access_key_id = config['DEFAULT']['AWS_ACCESS_KEY_ID']
            self.aws_secret_access_key = config['DEFAULT']['AWS_ACCESS_SECRET_KEY']
            self.get_ip = config['DEFAULT']['GET_IP']
            self.log = config['DEFAULT']['LOG']
        except:
            raise ConfigParserError('Load config file failed.')
