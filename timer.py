# -*- coding:utf-8 -*-
import time
from datetime import datetime


class Timer(object):

    def __init__(self, buyTime, sleepInterval=1):

        # '2018-09-28 22:45:50'
        self.buy_time = datetime.strptime(buyTime, "%Y-%m-%d %H:%M:%S")
        self.sleepInterval = sleepInterval

    def start(self):
        while True:
            now = datetime.now()
            if now >= self.buy_time:
                break
            else:
                print(now, ', sleep for', min(self.sleepInterval, (self.buy_time - now).total_seconds()))
                time.sleep(min(self.sleepInterval, (self.buy_time - now).total_seconds()))
