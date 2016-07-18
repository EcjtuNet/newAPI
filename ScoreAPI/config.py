#coding:utf-8
import cgi

# 用户名和密码
username = '2015211001000622'
password = 'a13479249166+'
year = 2015
term =2

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

form = cgi.FieldStorage()
if form.has_key('username') and form.has_key('password'):
    username = form['username'].value
    password = form['password'].value
    year = form['year'].value
    term = form['term'].value

if (len(username)<14) and (len(password)<6):
    jsonData.failedData(401,'用户名或密码错误')
