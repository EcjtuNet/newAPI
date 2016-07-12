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
from bs4 import BeautifulSoup


def captchaRecognize(img):
    #无限中值过滤噪点
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    #锐化等处理图片
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.convert('L')
    enhancer=ImageEnhance.Color(img);
    enhancer=enhancer.enhance(0);   #变成黑白
    enhancer=ImageEnhance.Contrast(enhancer);
    enhancer=enhancer.enhance(8);   #提高对比度
    img = enhancer
    #识别修改后的图片
    text = pytesser.image_to_string(img)
    #使用正则表达式过滤除数字以外的识别数据
    captach = re.findall('[0-9]',text)
    captcha =  ''.join(captach)
    return captcha

def loginRequest(username,password,headers,opener):
    # 验证码地址和post地址
    CaptchaUrl = "http://jwxt.ecjtu.jx.cn/servlet/code.servlet"
    PostUrl = 'http://jwxt.ecjtu.jx.cn/stuMag/Login_login.action'
    picture = opener.open(CaptchaUrl).read()
    # 用openr访问验证码地址,获取cookie
    local = open('cod.jpg', 'wb')
    local.write(picture)
    local.close()
    # 保存验证码到本地
    img = Image.open('cod.jpg')
    SecretCode = captchaRecognize(img)

    postData = {
            'UserName':username,
            'Password': password,
            'code':SecretCode
    }
    data = urllib.urlencode(postData)
    # 生成post数据 ?key1=value1&key2=value2的形式
    request = urllib2.Request(PostUrl, data, headers)
    # 构造request请求
    # 打开保存的验证码图片 输入
    try:
        response = opener.open(request)
        result = response.read()
        if result == '验证码错误':
            loginRequest(PostUrl,CaptchaUrl,headers,opener)
        else:
            return result
        # 打印登录后的页面
    except urllib2.HTTPError, e:
        print e.code

def regular(result):
    soup = BeautifulSoup(result)
    table = soup.find_all('table')
    return table
# 用户名和密码
username = '2015211001000116'
password = 'qq3396675'
# 将cookies绑定到一个opener cookie由cookielib自动管理
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

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
loginRequest(username,password,headers,opener)
response = opener.open('http://jwxt.ecjtu.jx.cn/scoreQuery/stuScoreQue_getStuScore.action')
result = response.read()
print regular(result)
