#coding:utf-8
import urllib2
import cookielib
import urllib
import re
import sys
import requests
import time
from subprocess import Popen
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import pytesser
import cookielib
import cStringIO

# def captchaRecognize(img):
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#     img = img.filter(ImageFilter.MedianFilter())
#
#
#     enhancer = ImageEnhance.Contrast(img)
#     img = enhancer.enhance(2)
#     img = img.convert('L')
#     enhancer=ImageEnhance.Color(img);
#     enhancer=enhancer.enhance(0);   #变成黑白
#     enhancer=ImageEnhance.Contrast(enhancer);
#     enhancer=enhancer.enhance(8);   #提高对比度
#     # enhancer=ImageEnhance.Sharpness(enhancer);
#     # enhancer=enhancer.enhance(20);  #锐化
#     img = enhancer
#
#     img.show()
#     text = pytesser.image_to_string(img)
#     print text
#     captach = re.findall('[0-9]',text)
#     captcha =  ''.join(captach)
#     return captcha
'''''模拟登录'''
reload(sys)
sys.setdefaultencoding("utf-8")
# 防止中文报错
CaptchaUrl = "http://jwxt.ecjtu.jx.cn/servlet/code.servlet"
PostUrl = 'http://jwxt.ecjtu.jx.cn/stuMag/Login_login.action'
# 验证码地址和post地址
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# 将cookies绑定到一个opener cookie由cookielib自动管理
username = '2015211001000116'
password = 'qq3396675'
# 用户名和密码
picture = opener.open(CaptchaUrl).read()
# 用openr访问验证码地址,获取cookie
local = open('cod.jpg', 'wb')
local.write(picture)
local.close()
# 保存验证码到本地
img = Image.open('cod.jpg')
SecretCode = raw_input('输入')
# 打开保存的验证码图片 输入
postData = {
        'UserName':username,
        'Password': password,
        'code':SecretCode
}
# 根据抓包信息 构造表单
headers = {
         'Accept':'*/*' ,
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
         'X-Requested-With':'XMLHttpRequest',
         'Referer':'http://jwxt.ecjtu.jx.cn/login.jsp',
         'Accept-Language':'zh-CN',
         'Accept-Encoding':'gzip, deflate',
         'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)like Gecko',
         'Host':'jwxt.ecjtu.jx.cn',
}
# 根据抓包信息 构造headers
data = urllib.urlencode(postData)
# 生成post数据 ?key1=value1&key2=value2的形式
request = urllib2.Request(PostUrl, data, headers)
# 构造request请求
try:
    response = opener.open(request)
    result = response.read().decode('gb2312')
    # 由于该网页是gb2312的编码，所以需要解码
    print result
    # 打印登录后的页面
except urllib2.HTTPError, e:
    print e.code
