#coding:utf-8
import loginRequest
import infoQuery
import jsonData
import config

loginRequest.request(config.username,config.password,config.headers)

classInfoList = infoQuery.getClassInfo(config.year,config.term)

jsonData.successData(classInfoList)
