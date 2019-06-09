# coding:utf-8
import hashlib
import qingGuo.config


username = "201730269"
passwd = "111111"
yzm = 'gbhg'
# 学校设定
identity_verification = '14045'
typeName = 'gb2312'


def md5sum(obj):
    # md5
    return hashlib.md5(obj.encode(typeName)).hexdigest()


def chkpwd(stu: str, pwd: str) -> str:
    # dsdsdsdsdxcxdfgfg
    return md5sum(stu + md5sum(pwd)[:30].upper() + identity_verification)[:30].upper()


def chkyzm(yzm: str) -> str:
    # fgfggfdgtyuuyyuuckjg
    return md5sum(md5sum(yzm.upper())[:30].upper() + identity_verification)[:30].upper()


# 密码加密
print(chkpwd(username, passwd))
# 验证码加密
print(chkyzm(yzm))
