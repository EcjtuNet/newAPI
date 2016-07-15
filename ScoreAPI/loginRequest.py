#coding:utf-8
import cookielib
import urllib2
import urllib
import socket
import captchaProcess
import jsonData
import config

# 将cookies绑定到一个opener cookie由cookielib自动管理
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

def request():
    #socket.setdefaulttimeout(2)
    #post地址
    PostUrl = 'http://jwxt.ecjtu.jx.cn/stuMag/Login_login.action'
    # 保存验证码到本地
    if saveCaptcha()==False:
        jsonData.failedData(404)
    #识别验证码
    img = captchaProcess.openImg('cod.jpg')
    captchaImg = captchaProcess.pictureProcess(img)
    captcha = captchaProcess.captchaRecognize(captchaImg)
    if captcha == 0:
        jsonData.failedData(500,'验证码识别失败')
    postData = {
            'UserName':config.username,
            'Password': config.password,
            'code':captcha
    }
    # 生成post数据 ?key1=value1&key2=value2的形式
    data = urllib.urlencode(postData)
    # 构造request请求
    request = urllib2.Request(PostUrl, data, config.headers)
    try:
        response = opener.open(request)
        result = response.read()
        if result == 'success':
            return True
        else:
            jsonData.failedData(503,'网页打开失败')
        # 打印登录后的页面
    except urllib2.HTTPError, e:
        jsonData.failedData(503)
    return True

# 将验证码存储于本地，返回是否存储成功
def saveCaptcha():
    CaptchaUrl = "http://jwxt.ecjtu.jx.cn/servlet/code.servlet"
    picture = readUrl(CaptchaUrl)
    # 用openr访问验证码地址,获取cookie
    local = open('cod.jpg', 'wb')
    local.write(picture)
    local.close()
    return True

#通过opener打开网页并返回读取的html内容
def readUrl(url):
    try:
        response = opener.open(url)
        result = response.read()
    except Exception as e:
        jsonData.failedData(404)
    return result
