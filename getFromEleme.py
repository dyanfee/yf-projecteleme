import requests
import time
import threading
import pymysql
import json


class GetFromEleme():
    def get(self):
        print("this is get Func!")
        res = requests.post('https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=8&track_id=&platform=0&sn=2a2e2d990f3b004d&theme_id=569&device_id=&refer_user_id=12034332')
        res.encoding = 'utf-8'
        print(res.text)
        with open("res.html",'w+') as f:
            f.writelines(res.text)
            f.close()
        print(res.content)


if __name__ == "__main__":
    test = GetFromEleme()
    test.get()