import hashlib
import requests
#校身份验证码
identity_verification = '14045'
typeName = 'gb2312'
def md5sum(obj):
    #md5
    return hashlib.md5(obj.encode(typeName)).hexdigest()
def chkpwd(stu,pwd):
    #dsdsdsdsdxcxdfgfg
    return md5sum(stu + md5sum(pwd)[:30].upper() + identity_verification)[:30].upper()
def chkyzm(yzm):
    #fgfggfdgtyuuyyuuckjg
    return md5sum(md5sum(yzm.upper())[:30].upper() + identity_verification)[:30].upper()
class encrypt:
    """
    加密输入以模拟登陆
    """
    type='gb2312'
    id = identity_verification
if __name__ == '__main__':
    print(chkpwd('201730269','111111'))