# -*- coding: utf-8 -*-

import logging
import logging.handlers
from ddns.config import Config

class Log:
    is_log = True

    logger = logging.getLogger('crumbs')
    logger.setLevel(logging.DEBUG)

    def __init__(self):
        config = Config()
        log_path = config.log

        formatter = logging.Formatter('[%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s] %(message)s')

        if str(log_path).upper() == 'CONSOLE':
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
        elif str(log_path).upper() == 'NONE':
            self.is_log = False
            return
        else:
            file_max_bytes = 10 * 1024 * 1024

            file_handler = logging.handlers.RotatingFileHandler(filename=log_path, maxBytes=file_max_bytes)
            stream_handler = logging.StreamHandler()

            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)

    @classmethod
    def write(cls, message):
        if cls.is_log:
            cls.logger.debug(message)
