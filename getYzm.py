# coding:utf-8

import requests
import time
from qingGuo.getCookie import getCookieByRequestUrl
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

def getYZMImage(url, cookie):
    """
    请求验证码的网址，下载验证码信息
    :param url: 验证码的链接
    :param cookie: cookie信息
    :return:
    """
    cookievalue = 'ASP.NET_SessionId=' + str(cookie)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
        'Cookie': cookievalue,
        'Referer': 'http://jwgl.ccswust.edu.cn/_data/login_home.aspx',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Accept-Encoding':' gzip, deflate',
        'Accept': 'image/webp,*/*',
        'Host': 'jwgl.ccswust.edu.cn',
    }
    response = requests.get(url=url, headers=headers)
    captcha(response.content)


def captcha(data):
    """
    保存验证码图片到本地
    :param data:
    :return:
    """
    with open('captcha.jpg', 'wb') as fp:
        fp.write(data)
    time.sleep(1)


cookie = getCookieByRequestUrl("http://jwglxt.aynu.edu.cn/",headers=headers)
#
url = "http://jwglxt.aynu.edu.cn/sys/ValidateCode.aspx?t=121"
 getYZMImage(url=url,cookie=cookie)