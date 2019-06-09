# coding:utf-8

import requests


username = "201730269"
passwd = "111111"
yzm = 'gbhg'
# 学校设定
identity_verification = '14045'
typeName = 'gb2312'
urlS: str = 'http://jwgl.ccswust.edu.cn/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}


def getCookieByRequestUrl(response):
    """
    根据请求的响应获取cookie信息
    :param response: 请求网站后的响应
    :return:
    """
    cookiejar = response.cookies

    # 8. 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

    return cookiedict['ASP.NET_SessionId']

    # print cookiejar
    #
    # print cookiedict


def getCookieByRequestSession(url, headers):
    """
    发送请求获取cookie信息
    :param url: 请求的网站的网址
    :param headers: 请求头
    :return:
    """
    session = requests.session()
    response = session.get(url=url, headers=headers)
    cookiedict = requests.utils.dict_from_cookiejar(response.cookies)
    return cookiedict['ASP.NET_SessionId']


print(getCookieByRequestUrl(urlS))
print(getCookieByRequestSession(urlS, headers=headers))
