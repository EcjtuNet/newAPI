#coding:utf-8
import loginRequest
import infoQuery
import jsonData
import config

loginRequest.request(config.username,config.password,config.headers)

scoreInfoList = infoQuery.getScoreInfo(config.year,config.term)

jsonData.successData(scoreInfoList)
