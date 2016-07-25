##coding:utf-8
from bs4 import BeautifulSoup
import loginRequest
import re

def getExamInfo(year,term,username):

    queryTerm = str(year)+'.'+str(term)
    queryUrl = 'http://jwxt.ecjtu.jx.cn/examArrange/stuExam_stuQueryExam.action?term='+queryTerm+'&userName='+username

    html = loginRequest.readUrl(queryUrl)
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find("table",class_="table_border")
    trList = table.find_all('tr')

    examInfoList = []
    #不抓取第一行table头
    for i in range(1,len(trList)-1):
        tdList = trList[i].find_all('td')

        singleExamInfoList = []

        for j in range(8):
            singleExamInfoList = {
                '课程名称':tdList[1].string,
                '课程性质':tdList[2].string,
                '班级名称':tdList[3].string,
                '学生人数':tdList[4].string,
                '考试周次':tdList[5].string,
                '考试时间':tdList[6].string,
                '考试地点':tdList[7].string
            }
        examInfoList.append(singleExamInfoList)

    return examInfoList
