#coding:utf-8
import loginRequest
import infoQuery
import jsonData
import config

loginRequest.request(config.username,config.password,config.headers)

scoreInfoList = infoQuery.getExamInfo(config.year,config.term,config.username)

jsonData.successData(scoreInfoList)
