# -*- coding: utf-8 -*-

import logging
import logging.handlers

class Log:
    logger = logging.getLogger('crumbs')
    logger.setLevel(logging.DEBUG)

    def __init__(self):
        formatter = logging.Formatter('[%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s] %(message)s')
        file_max_bytes = 10 * 1024 * 1024

        file_handler = logging.handlers.RotatingFileHandler(filename='./log/test.log', maxBytes=file_max_bytes)
        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    @classmethod
    def write(cls, message):
        cls.logger.debug(message)
