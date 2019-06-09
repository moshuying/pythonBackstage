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

    LoginUrl = 'http://jwgl.ccswust.edu.cn'
    Data = {
        "__VIEWSTATE":"/wEPDwUKMTAzNTIzMjg1NWRk"
        ,"__EVENTVALIDATION":"/wEWAgLWvs6TCwKZwe+vBg=="
        ,"pcInfo":"Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64;+rv:68.0)+Gecko/20100101+Firefox/68.0Windows+NT+10.0;+Win64;+x645.0+(Windows)+SN:NULL"
        ,"txt_mm_expression":""
        ,"txt_mm_length":""
        ,"txt_mm_userzh":""
        ,"typeName":"%D1%A7%C9%FA"
        ,"dsdsdsdsdxcxdfgfg": chkpwd('201730269','111111')
        , "fgfggfdgtyuuyyuuckjg": chkyzm('111111')
        ,"Sel_Type":"STU"
        ,"txt_asmcdefsddsd":'201730269'
        ,"txt_pewerwedsdfsdff":""
        ,"txt_psasas":"%C7%EB%CA%E4%C8%EB%C3%DC%C2%EB"
        ,"txt_sdertfgsadscxcadsads":""
        }
    Headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    Res = requests.post(LoginUrl, data=Daquta, headers=Headers)
    print(Res.text)