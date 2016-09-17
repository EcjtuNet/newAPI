import json

def failedData(statementCode,msg):
    data = {
        'code':statementCode,
        'msg':msg
    }
    jsonData = json.dumps(data)
    return jsonData
    exit()

def successData(result):
    data = {
        'code':200,
        'msg':'success',
        'result':result
    }
    jsonData = json.dumps(data)
    return jsonData
    exit()
