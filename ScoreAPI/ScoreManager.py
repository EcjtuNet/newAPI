from bs4 import BeautifulSoup

class Score(object):

    def __init__(self,result):
        self.soup = BeautifulSoup(result)
        # table = soup.find_all("ul",class_= "2015_1 term_score")

    def getScoreInfo(self):
        originScoreInfoList = self.soup.find_all("ul",class_= "2015_1 term_score")

        scoreInfoList = {}
        for originScoreInfo in originScoreInfoList:
            scoreInfo = {}
            scoreInfo['object'] = originScoreInfo[1]
            scoreInfo['object'] = originScoreInfo[1]
            scoreInfo['object'] = originScoreInfo[1]
            scoreInfo['object'] = originScoreInfo[1]
            scoreInfoList.append(scoreInfo)
