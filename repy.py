from urllib.parse import unquote
import re
import requests
import json


class Cookie:
    def __init__(self, jurl, snsinfo, utrace, ubt_ssid, perf_ssid, SID, sign):
        self.jurl = jurl
        self.snsinfo = snsinfo
        self.utrace = utrace
        self.ubt_ssid = ubt_ssid
        self.perf_ssid = perf_ssid
        self.SID = SID
        self.sign = sign


# 返回sn字符串 group_sn
def isSN(url):
    pattern = re.compile(r'&sn=(.*?)&', re.S)
    sn = re.findall(pattern, url)
    # 如果只有一个就返回一个sn的字符串，如果多个，就返回list
    if len(sn) == 1:
        for i in sn:
            sn = i
        if sn:
            return sn
    elif len(sn) > 1:
        return sn
    else:
        return None


# 返回luck_number字符串
def isLuckNumber(url):
    pattern = re.compile(r'lucky_number=(.*?)&', re.S)
    lucknumber = re.findall(pattern, url)
    for i in lucknumber:
        lucknumber = i
    if lucknumber:
        if lucknumber == 0 or lucknumber == '0':
            group_sn = isSN(url)
            # luck_url = "https://h5.ele.me/restapi/marketing/themes/3137/group_sns/"
            luck_url = "https://h5.ele.me/restapi/marketing/themes/"
            luck_url = luck_url + isTheme_id(url)
            luck_url = luck_url + '/group_sns/' + group_sn
            lucknumber = requests.get(luck_url).content.decode()
            print(lucknumber)
            lucknumber_dict = json.loads(lucknumber)
            try:
                lucknumber = lucknumber_dict['lucky_number']
            except:
                print("获取lucknumber失败，红包链接不正确")
        return lucknumber
    else:
        return None


# 返回theme_id=2985
def isTheme_id(url):
    pattern = re.compile(r'&theme_id=(.*?)&', re.S)
    sn = re.findall(pattern, url)
    # 如果只有一个就返回一个sn的字符串，如果多个，就返回list
    if len(sn) == 1:
        for i in sn:
            sn = i
        if sn:
            return sn
    elif len(sn) > 1:
        return sn
    else:
        return None


# 返回elemekey 字符串 即sign
def iselemekey(cookiestr):
    pattern = re.compile(r'eleme_key%22%3A%22(.*?)%22%2C%22', re.S)
    elemekey = re.findall(pattern, cookiestr)
    for i in elemekey:
        elemekey = i
    if elemekey:
        return elemekey
    else:
        return None


# 返回jurl的字符串
def isJurl(cookiestr):
    pattern = re.compile(r'openid%22%3A%22(.*?)%22%2C%22', re.S)
    reurl = "https://h5.ele.me/restapi/marketing/promotion/weixin/"
    jurl = re.findall(pattern, cookiestr)
    for i in jurl:
        jurl = i
    if jurl:
        return reurl + jurl
    else:
        return None


# isSid 确认是否有sid
# 返回cookie中的_utrace字段值
def is_utrace(cookiestr):
    pattern = re.compile(r'_utrace=(.*?);', re.S)
    _utrace = re.findall(pattern, cookiestr)
    for i in _utrace:
        _utrace = i
    if _utrace:
        return _utrace
    else:
        return None


# 返回cookie中的ubt_ssid字段值
def isUbt_ssid(cookiestr):
    pattern = re.compile(r'ubt_ssid=(.*?);', re.S)
    ubt_ssid = re.findall(pattern, cookiestr)
    for i in ubt_ssid:
        ubt_ssid = i
    if ubt_ssid:
        return ubt_ssid
    else:
        return None


# 返回cookie中的perf_ssid字段值
def isPerf_ssid(cookiestr):
    pattern = re.compile(r'perf_ssid=(.*?);', re.S)
    perf_ssid = re.findall(pattern, cookiestr)
    for i in perf_ssid:
        perf_ssid = i
    if perf_ssid:
        return perf_ssid
    else:
        return None


# 返回cookie中的SID字段值
def isSID(cookiestr):
    pattern = re.compile(r'SID=(.*?);', re.S)
    SID = re.findall(pattern, cookiestr)
    for i in SID:
        SID = i
    if SID:
        return SID
    else:
        return None


# "avatar%22%3A%22http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA/132%22%7D"
def is_avater(ck):
    pass

# snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E4%B8%89%E6%98%8E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%22f34edcff1fd1e340d05e898315649169%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22openid%22%3A%22oEGLvjmhOfcGWsb1v6YHycaKX42M%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuAmRjzGvanB7E5xQ3ysQMqw%22%2C%22name%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%7D


def is_snsinfo(ck):
    pattern = re.compile(r'snsInfo.*?(?=;)')
    snsinfo = re.findall(pattern, ck)[0].split("=")
    if snsinfo:
        return snsinfo
    else:
        return None


def main(url, ck):

    jurl = isJurl(ck)
    snsinfo = is_snsinfo(ck)
    utrace = is_utrace(ck)
    ubt_ssid = isUbt_ssid(ck)
    perf_ssid = isPerf_ssid(ck)
    SID = isSID(ck)
    sign = iselemekey(ck)
    cookie = Cookie(jurl, snsinfo, utrace, ubt_ssid, perf_ssid, SID, sign)
    return cookie


if __name__ == '__main__':
    cookiestr = 'perf_ssid=l3p4vpbkzivgf6vxmvway4915i542cq0_2019-04-01; ubt_ssid=k823pvarpm3ko5vr9fd2y8t46opzzk19_2019-04-01; cna=TwopFbjmrX0CAXAFyZiNggaD; snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E4%B8%89%E6%98%8E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%22f34edcff1fd1e340d05e898315649169%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22openid%22%3A%22oEGLvjmhOfcGWsb1v6YHycaKX42M%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuAmRjzGvanB7E5xQ3ysQMqw%22%2C%22name%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%7D; _utrace=f699bb897cd20edb2fc6b3c80488da3d_2019-04-01; track_id=1554128000|5ecd3a2df59d2233882f8e789bf3c464a090c1317abe4e425f|8a9be4ac1239464734b67b7dba8f0ccd; USERID=7681242; UTUSER=7681242; SID=4Uy0lFhJ2FTJ7tOYsdblwLJlMCETBmjNzMxA; isg=BHh4kvLbUHnEg7z9SIaeSy4yXCYK4dxrU1m7SrLo6LNszRi3WvMI-41mgYVYmJRD'
    url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=0&track_id=&platform=0&sn=2a2c404aff38783d&theme_id=3931&device_id=&refer_user_id=69939721'
    # print(isJurl(cookiestr))
    # print(isSN(url))
    # print(iselemekey(cookiestr))
    # print(isSID(cookiestr))
    print(main(url, cookiestr))
