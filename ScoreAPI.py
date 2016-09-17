
##coding:utf-8
from bs4 import BeautifulSoup
import loginRequest
import re

def getScoreInfo(year,term):

    html = loginRequest.readUrl('http://jwxt.ecjtu.jx.cn/scoreQuery/stuScoreQue_getStuScore.action')

    soup = BeautifulSoup(html,"html.parser")
    originScoreInfoList = soup.find_all("ul",class_= str(year)+'_'+str(term)+" term_score")
    
    scoreInfoList = []
    for originScoreInfo in originScoreInfoList:
        item = originScoreInfo.find_all('li')
        scoreInfo = {
            'objectName':item[1].string,
            'classRequirement':item[2].string,
            'assessment':item[3].string,
            'credit':item[4].string,
            'score':item[5].string
        }
        scoreInfoList.append(scoreInfo)
    return scoreInfoList
