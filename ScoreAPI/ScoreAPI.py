#coding:utf-8
import re
import requests
from subprocess import Popen
import PictureRecognize
import Login
import ScoreManager
import json
import cgi

def loginInfoIsCorrect(username,password):
    if (len(username)>=14) and (len(password)>=6):
        return True
    else:
        return False

# 用户名和密码
username = '2015211001000622'
password = 'a13479249166+'
#从form获取用户名和密码
form = cgi.FieldStorage()
if form.has_key('username') and form.has_key('password'):
    username = form['username'].value
    password = form['password'].value
    year = form['year'].value
    term = form['term'].value

#头文件
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

isSuccess = Login.loginRequest(username,password,headers)
data = {}
if loginInfoIsCorrect(username,password) == False:
        data = {
            'code':422,
            'smg':'failed'
        }
elif isSuccess:
    result = Login.readUrl('http://jwxt.ecjtu.jx.cn/scoreQuery/stuScoreQue_getStuScore.action')
    score = ScoreManager.Score(result)
    scoreInfoList = score.getScoreInfo(2015,2)
    data = {
        'code':200,
        'msg':'success',
        'result':scoreInfoList
    }
else:
    data = {
        'code':400,
        'msg':'error'
    }

jsonData = json.dumps(data)
print jsonData
