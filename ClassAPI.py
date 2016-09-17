##coding:utf-8
from bs4 import BeautifulSoup
import loginRequest
import re

def getClassInfo(year,term):

    queryUrl = 'http://jwxt.ecjtu.jx.cn/Schedule/Schedule_getUserSchedume.action?term='+str(year)+'.'+str(term)
    html = loginRequest.readUrl('http://jwxt.ecjtu.jx.cn/Schedule/Schedule_getUserSchedume.action')

    soup = BeautifulSoup(html,"html.parser")
    #获取包含课程信息的table内容
    table = soup.find("table",class_="table_border",id="courseSche")
    #获取行内容
    trList = table.find_all('tr')
    #用于存储一周的课程信息，数组中每个对象都是存储每天第N节课的数组
    classInfoList = []
    #获取一周内每天第N节课的课程内容
    for i in [1,2,3,4,5,6]:
        originClassInfo = trList[i].find_all('td')
        #用于存储每天第N节课的内容，单个对象是单节课信息
        singleClassInfoList = []
        #处理每天第N节课的课程内容
        for j in [1,2,3,4,5,6,7]:
            singleClassInfo = originClassInfo[j].get_text().replace('</br>',' ')
            singleClassInfoList.append(singleClassInfo)
        classInfoList.append(singleClassInfoList)
    #数组转置，NB的大反转！！将存储每天第N节课内容的的矩阵转置成存储单天课程信息的单一数组
    monday,tuesday,wednesday,thursday,friday,saturday,sunday = zip(*classInfoList)

    classInfo = {
        'monday':monday,
        'tuesday':tuesday,
        'wednesday':wednesday,
        'thursday':thursday,
        'friday':friday,
        'saturday':saturday,
        'sunday':sunday
    }
    return classInfo
