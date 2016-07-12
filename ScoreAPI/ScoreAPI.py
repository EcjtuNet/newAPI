#coding:utf-8
import re
import requests
from subprocess import Popen
import PictureRecognize
import Login
import ScoreManager


# 用户名和密码
username = '2015211001000116'
password = 'qq3396675'

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
Login.loginRequest(username,password,headers)
result = Login.readUrl('http://jwxt.ecjtu.jx.cn/scoreQuery/stuScoreQue_getStuScore.action')
score = ScoreManager.Score(result)
score.getScoreInfo()
print score[0].find_all('li')[3]
