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

s = 'perf_ssid=w7n3r45auevcuvy21hzzzxmuarj28nc1_2019-04-01; ubt_ssid=6merjdf5lsepr3imiwy4z8b3icl3o0jf_2019-04-01; cna=QOcoFWKlmEACAToXEVKShamJ; snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E6%B3%89%E5%B7%9E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%225d827bdacb03408ceded7f033f73bba1%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJiaCBO9f33YY8H8Myu0CPY7Ioqo78fs1Q1L2KOBbIiaGYibhyhMICdeZGDO3nW6HcOP5kX21LF3jyAA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22DDDDDD%22%2C%22openid%22%3A%22oEGLvjsVNc-c6e_pzoOdvtEa5R84%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuFmsYCfdeWQTAIc-RILRS_I%22%2C%22name%22%3A%22DDDDDD%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJiaCBO9f33YY8H8Myu0CPY7Ioqo78fs1Q1L2KOBbIiaGYibhyhMICdeZGDO3nW6HcOP5kX21LF3jyAA%2F132%22%7D; _utrace=7359a3a5f834c5f087841933971fd6f0_2019-04-01; track_id=1554119006|a66ff561350004fef4ef25ad1c80dcad6ec73a8fd12c63555a|b967579a57648bfa223803b79105a53c; USERID=12034332; UTUSER=12034332; SID=wuBkKFh2SCzJm85MhtOzvk8DEf4fIOcpSDIQ; isg=BEREPAmOxJYjXnDa9j5rzth5AMI2XWjH2Fwu6l7nhI_WieBTl2wZVWiizWH0kaAf'
if __name__ == "__main__":
    test = GetFromEleme()
    test.get()