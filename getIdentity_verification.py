import urllib.request
import re
from urllib import parse
from urllib.request import urlopen
typeName='utf-8'
def loadPage(url,filename):
    return urlopen(url).read().decode(typeName)
def getPage(url):
    fullurl=url+'/home.aspx'
    header = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.")
    urllib.request.build_opener().addheaders = [header]
    urllib.request.install_opener(urllib.request.build_opener())
    data = re.compile("substring\(0,30\).toUpperCase\(\)\+'(.*?)'\)\.substring").findall(urllib.request.urlopen(fullurl).read().decode())
    return data
if __name__ == '__main__':
    url='http://jwgl.ccswust.edu.cn'
    print(getPage(url))