import requests
import re


# 返回 group_sn
def sn(url):
    pattern = re.compile(r'&sn=(.*?)&', re.S)
    sn = re.findall(pattern, url)
    if len(sn) == 1:
        for i in sn:
            sn = i
        if sn:
            return sn
    elif len(sn) > 1:
        return sn
    else:
        return None


# 返回sign
def sign(ck):
    pattern = re.compile(r'eleme_key%22%3A%22(.*?)%22%2C%22', re.S)
    elemekey = re.findall(pattern, ck)
    for i in elemekey:
        elemekey = i
    if elemekey:
        return elemekey
    else:
        return None


if __name__ == '__main__':
    url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=8&track_id=&platform=0&sn=2a2e0bbbc4bb000a&theme_id=569&device_id=&refer_user_id=12034332'
    ck = 'perf_ssid=l3p4vpbkzivgf6vxmvway4915i542cq0_2019-04-01; ubt_ssid=k823pvarpm3ko5vr9fd2y8t46opzzk19_2019-04-01; cna=TwopFbjmrX0CAXAFyZiNggaD; snsInfo[wx2a416286e96100ed]=%7B%22city%22%3A%22%E4%B8%89%E6%98%8E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22eleme_key%22%3A%22f34edcff1fd1e340d05e898315649169%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%2C%22language%22%3A%22zh_CN%22%2C%22nickname%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22openid%22%3A%22oEGLvjmhOfcGWsb1v6YHycaKX42M%22%2C%22privilege%22%3A%5B%5D%2C%22province%22%3A%22%E7%A6%8F%E5%BB%BA%22%2C%22sex%22%3A1%2C%22unionid%22%3A%22o_PVDuAmRjzGvanB7E5xQ3ysQMqw%22%2C%22name%22%3A%22%E5%90%B4%E5%BB%BA%E5%8D%8E%F0%9F%94%A5%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTI1tic4EUrqj5NmaHR9zXJcJYr4IWHrqnS8jN50YZUdgdvVTp3kpTXFCWBWc4XUrCbIugWlUficevEA%2F132%22%7D; _utrace=f699bb897cd20edb2fc6b3c80488da3d_2019-04-01; track_id=1554128000|5ecd3a2df59d2233882f8e789bf3c464a090c1317abe4e425f|8a9be4ac1239464734b67b7dba8f0ccd; USERID=7681242; UTUSER=7681242; SID=4Uy0lFhJ2FTJ7tOYsdblwLJlMCETBmjNzMxA; isg=BHh4kvLbUHnEg7z9SIaeSy4yXCYK4dxrU1m7SrLo6LNszRi3WvMI-41mgYVYmJRD'
    print(sn(url))
    print(sign(ck))
