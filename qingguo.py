import hashlib
import requests
id=identity_verification = '14045'

def md5sum(obj):
    md5 = hashlib.md5(obj.encode('gb2312')).hexdigest()
    return md5
def chkpwd(stu,pwd):
    s=md5sum(pwd+md5sum(stu)[:30].upper()+'14045')[:30].upper()
    dsdsdsdsdxcxdfgfg = s
    return dsdsdsdsdxcxdfgfg
class encrypt:
    """
    加密输入以模拟登陆
    """
    type='gb2312'
    id = identity_verification
    def md5sum(self):
        md5=hashlib.md5(self.id.encode(self.type)).hexdigest()
        return md5
    def __init__(self,stu,pwd,yzm):
        self.pwd=pwd
        self.stu=stu
        self.yzm=yzm
    def chkpwd(self):
        s = self.md5sum(self.stu +self.md5sum(self.pwd)[:30].upper() + id )[:30].upper()
        dsdsdsdsdxcxdfgfg = s
        return dsdsdsdsdxcxdfgfg
    def chkyzm(self):
        """
        :param : 验证码加密
        :return: 返回加密后的验证码
        """
        s = self.md5sum(self.md5sum(self.yzm.upper())[:30].upper() + id )[:30].upper()
        fgfggfdgtyuuyyuuckjg = s
        return fgfggfdgtyuuyyuuckjg
def getContent(url):
    result=requests.get(url)
    return result.content
def getlogin(url):
    content=getContent(url)
# login = encrypt('201730269','11111','ABCD')
#登陆加密方式

print(chkpwd('201730269','111111'))
#验证码加密
# print(login.chkyzm('xzv5'))