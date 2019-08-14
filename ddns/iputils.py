# -*- coding: utf-8 -*-

import socket
from urllib.request import urlopen
from bs4 import BeautifulSoup

class IPUtils:
    @staticmethod
    def getrealip():
        html = urlopen("http://bot.whatismyipaddress.com")
        current_ip = BeautifulSoup(html, "html.parser")
        return str(current_ip)

    @staticmethod
    def getlocalip(type):
        if type == 1:
            return str(socket.gethostbyname(socket.gethostname()))
        elif type == 2:
            return str(socket.gethostbyname_ex(socket.gethostname()))
        else:
            return str(socket.gethostbyname(socket.getfqdn()))