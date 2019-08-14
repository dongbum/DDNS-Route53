# -*- coding: utf-8 -*-

class IPcheckError(Exception):
    def __init__(self, msg):
        self.msg = msg

class ConfigParserError(Exception):
    def __init__(self, msg):
        self.msg = msg