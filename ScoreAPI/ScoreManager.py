##coding:utf-8
from bs4 import BeautifulSoup

class Score(object):

    def __init__(self,result):
        self.soup = BeautifulSoup(result,"html.parser")
        # table = soup.find_all("ul",class_= "2015_1 term_score")

    def getScoreInfo(self,year,term):
        term_info = str(year)+'_'+str(term)
        originScoreInfoList = self.soup.find_all("ul",class_= term_info+" term_score")

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
