# -*- coding: utf-8 -*-

import os

class RecordFile:

    # 파일이 이미 존재하면 아이피를 읽어서 리턴한다.
    # 파일이 존재하지 않는다면 파일을 생성하고 현재 아이피를 추가하고 리턴한다.
    @staticmethod
    def get_old_ip(current_ip):
        try:
            if os.path.exists('old_ip.txt'):
                f = open('old_ip.txt', mode='rt', encoding='utf-8')
                old_ip = f.read()
                f.close()

                return old_ip
            else:
                f = open('old_ip.txt', mode='wt', encoding='utf-8')
                f.write(str(current_ip))
                f.close()

                return current_ip
        except:
            print('file exception')
            return '127.0.0.1'
