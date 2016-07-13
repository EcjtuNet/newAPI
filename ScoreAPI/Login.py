#coding:utf-8
import urllib2
import cookielib
import urllib
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import pytesser
import re
import socket

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

# 将cookies绑定到一个opener cookie由cookielib自动管理

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
    captcha = re.findall('[0-9]',text)
    captcha =  ''.join(captcha)
    print captcha
    return captcha

def loginRequest(username,password,headers):
    #socket.setdefaulttimeout(2)

    # 验证码地址和post地址
    CaptchaUrl = "http://jwxt.ecjtu.jx.cn/servlet/code.servlet"
    PostUrl = 'http://jwxt.ecjtu.jx.cn/stuMag/Login_login.action'
    try:
        captchaRequest = opener.open(CaptchaUrl,timeout = 2)
    except urllib2.HTTPError, e:
        return False
    # 用openr访问验证码地址,获取cookie
    picture = captchaRequest.read()
    local = open('cod.jpg', 'wb')
    local.write(picture)
    local.close()
    # 保存验证码到本地
    img = Image.open('cod.jpg')
    captcha = captchaRecognize(img)

    postData = {
            'UserName':username,
            'Password': password,
            'code':captcha
    }
    data = urllib.urlencode(postData)
    # 生成post数据 ?key1=value1&key2=value2的形式
    request = urllib2.Request(PostUrl, data, headers)
    # 构造request请求
    try:
        response = opener.open(request)
        result = response.read()
        if result == 'success':
            return True
        else:
            return False
        # 打印登录后的页面
    except urllib2.HTTPError, e:
        return False

def readUrl(url):
    response = opener.open(url)
    result = response.read()
    return result
