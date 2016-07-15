#coding:utf-8
import loginRequest
import infoQuery
import jsonData
import config

if (len(config.username)<14) and (len(config.password)<6):
    jsonData.failedData(401,'用户名或密码错误')
loginRequest.request()
classInfoList = infoQuery.getClassInfo(2015,1)
jsonData.successData(classInfoList)
