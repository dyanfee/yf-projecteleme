import requests
import time
import threading
# import pymysql
import json
import re
import cookie

class GetFromEleme():
    def get(self):
        print("this is get Func!")
        res = requests.post(
            'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=5&track_id=&platform=0&sn=2a2e0c2cc8bb0034&theme_id=569&device_id=&refer_user_id=12034332')
        res.encoding = 'utf-8'
        print(res.text)
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080'}

        with open("res.html", 'w+') as f:
            f.writelines(res.text)
            f.close()
        print(res.content)

    def initUser(self, configName):
        user = {}
        user['nickname'] = conf.get(configName, 'nickname')
        user['cookies'] = {}
        UserCookies = conf.get(configName, 'cookies').replace(' ', '')
        for cookie in UserCookies.split(';'):
            kv = cookie.split('=')
            user['cookies'][kv[0]] = kv[1]
            if 'snsInfo' in kv[0]:
                user['sign'] = re.findall(
                    '(?<=eleme_key%22%3A%22).+?(?=%22%2C%22)', kv[1])[0]
                user['openid'] = re.findall(
                    '(?<=openid%22%3A%22).+?(?=%22%2C%22)', kv[1])[0]
                user['unionid'] = re.findall(
                    '(?<=unionid%22%3A%22).+?(?=%22%2C%22)', kv[1])[0]
                user['weixin_avatar'] = unquote(re.findall(
                    '(?<=headimgurl%22%3A%22).+?(?=%22%2C%22)', kv[1])[0])
                requestData(user)
        return user
    def cookie_find(self,userinfo):
        # user_cookie = cookie.Cookie()
        user = userinfo.replace(' ','')
        for each in user.split(';'):
            print(each)
            perf_ssid

    def find_tool(self, url):
        lucky_num = int(
            re.search(r'(?<=lucky_number=).+(?=&track_id)', str(url)).group())
        print(lucky_num)


s = 'perf_ssid=w7n3r45auevcuvy21hzzzxmuarj28nc1_2019-04-01; ubt_ssid=6merjdf5lsepr3imiwy4z8b3icl3o0jf_2019-04-01; cna=QOcoFWKlmEACAToXEVKShamJ; snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E6%B3%89%E5%B7%9E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%225d827bdacb03408ceded7f033f73bba1%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJiaCBO9f33YY8H8Myu0CPY7Ioqo78fs1Q1L2KOBbIiaGYibhyhMICdeZGDO3nW6HcOP5kX21LF3jyAA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22DDDDDD%22%2C%22openid%22%3A%22oEGLvjsVNc-c6e_pzoOdvtEa5R84%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuFmsYCfdeWQTAIc-RILRS_I%22%2C%22name%22%3A%22DDDDDD%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJiaCBO9f33YY8H8Myu0CPY7Ioqo78fs1Q1L2KOBbIiaGYibhyhMICdeZGDO3nW6HcOP5kX21LF3jyAA%2F132%22%7D; _utrace=7359a3a5f834c5f087841933971fd6f0_2019-04-01; track_id=1554119006|a66ff561350004fef4ef25ad1c80dcad6ec73a8fd12c63555a|b967579a57648bfa223803b79105a53c; USERID=12034332; UTUSER=12034332; SID=wuBkKFh2SCzJm85MhtOzvk8DEf4fIOcpSDIQ; isg=BEREPAmOxJYjXnDa9j5rzth5AMI2XWjH2Fwu6l7nhI_WieBTl2wZVWiizWH0kaAf'
if __name__ == "__main__":
    test = GetFromEleme()
    # test.get()
    ur = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=0&track_id=&platform=0&sn=2a2c404aff38783d&theme_id=3931&device_id=&refer_user_id=69939721'
    url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=8&track_id=&platform=0&sn=2a2e0bbbc4bb000a&theme_id=569&device_id=&refer_user_id=12034332'
    # test.find_tool(url)
    cookie = r'perf_ssid=l3p4vpbkzivgf6vxmvway4915i542cq0_2019-04-01; ubt_ssid=k823pvarpm3ko5vr9fd2y8t46opzzk19_2019-04-01; cna=TwopFbjmrX0CAXAFyZiNggaD; snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E4%B8%89%E6%98%8E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%22f34edcff1fd1e340d05e898315649169%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22openid%22%3A%22oEGLvjmhOfcGWsb1v6YHycaKX42M%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuAmRjzGvanB7E5xQ3ysQMqw%22%2C%22name%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%7D; _utrace=f699bb897cd20edb2fc6b3c80488da3d_2019-04-01; track_id=1554128000|5ecd3a2df59d2233882f8e789bf3c464a090c1317abe4e425f|8a9be4ac1239464734b67b7dba8f0ccd; USERID=7681242; UTUSER=7681242; SID=4Uy0lFhJ2FTJ7tOYsdblwLJlMCETBmjNzMxA; isg=BHh4kvLbUHnEg7z9SIaeSy4yXCYK4dxrU1m7SrLo6LNszRi3WvMI-41mgYVYmJRD'
    test.cookie_find(cookie)