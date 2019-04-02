import requests
import time
import threading
# import pymysql
import json
import re
import cookie
import repy


class GetFromEleme():
    def writefile(self, content):
        with open("res.json", "w+") as f:
            f.writelines(content)
            f.close()

    # 领取红包

    def get_one(self, url, ck):
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080'}
        jurl = repy.isJurl(ck)

        # cookie字典
        cookiedict = {}
        snsinfo = repy.is_snsinfo(ck)
        cookiedict[snsinfo[0]] = snsinfo[1]
        cookiedict['_utrace'] = repy.is_utrace(ck)
        cookiedict['ubt_ssid'] = repy.isUbt_ssid(ck)
        cookiedict['perf_ssid'] = repy.isPerf_ssid(ck)
        cookiedict['SID'] = repy.isSID(ck)
        # for key, value in cookiedict.items():
        #     print(key, ' : ', type(value))

        # json字典
        jsondict = {'group_sn': '',
                    'sign': '',
                    'weixin_avatar': 'http://thirdqq.qlogo.cn/qqapp/101204453/6409FAE1CEA4B1A50F8A85B8DFDA7236/40',
                    'weixin_username': 'DAXIGUA',
                    'method': 'phone'}
        jsondict["group_sn"] = repy.isSN(url)
        jsondict["sign"] = repy.iselemekey(ck)

        # for key, value in jsondict.items():
        #     print(key,' : ',value)

        s = requests.session()
        re = s.post(url=jurl, headers=headers,
                    cookies=cookiedict, json=jsondict)
        re_json = re.content.decode()
        # print(re_json)

        # json对象解析为字典
        re_json_dict = json.loads(re_json)
        # self.writefile(re_json)
        if (len(re_json_dict) != 2):
            arrlen = len(re_json_dict['promotion_records'])
            print("已经领取个数："+str(arrlen))
        else:
            arrlen = -1
            message = re_json_dict['message']
            print("返回json错误：" + message)
            print("当前cookieid：" + str(ck))
        return int(arrlen)

        def get_max(url, ck):
            lucky_number = repy.isLuckNumber(url)
            if lucky_number != None:
                print("手气最佳位置:"+str(lucky_number))
            else：
                print("获取手气最佳失败！")
                return
            

if __name__ == "__main__":
    test = GetFromEleme()
    # test.get()
    url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=0&track_id=&platform=0&sn=1d3b1d1ef08550cc&theme_id=3979&device_id=&refer_user_id=6539612'
    cookie = 'perf_ssid=l3p4vpbkzivgf6vxmvway4915i542cq0_2019-04-01; ubt_ssid=k823pvarpm3ko5vr9fd2y8t46opzzk19_2019-04-01; cna=TwopFbjmrX0CAXAFyZiNggaD; snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E4%B8%89%E6%98%8E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%22f34edcff1fd1e340d05e898315649169%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22openid%22%3A%22oEGLvjmhOfcGWsb1v6YHycaKX42M%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuAmRjzGvanB7E5xQ3ysQMqw%22%2C%22name%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%7D; _utrace=f699bb897cd20edb2fc6b3c80488da3d_2019-04-01; track_id=1554128000|5ecd3a2df59d2233882f8e789bf3c464a090c1317abe4e425f|8a9be4ac1239464734b67b7dba8f0ccd; USERID=7681242; UTUSER=7681242; SID=4Uy0lFhJ2FTJ7tOYsdblwLJlMCETBmjNzMxA; isg=BHh4kvLbUHnEg7z9SIaeSy4yXCYK4dxrU1m7SrLo6LNszRi3WvMI-41mgYVYmJRD'
    test.get_one(url, cookie)
