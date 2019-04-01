import requests
import time
import threading
import pymysql
import json


class GetFromEleme():
    def get(self):
        print("this is get Func!")
        res = requests.get('')
