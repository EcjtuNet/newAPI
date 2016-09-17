import flask
import loginRequest
import jsonData
import ScoreAPI
import ClassAPI
import ExamAPI

headers = {
         'Accept':'*/*' ,
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
         'X-Requested-With':'XMLHttpRequest',
         'Referer':'http://jwxt.ecjtu.jx.cn/login.jsp',
         'Accept-Language':'zh-CN',
         'Accept-Encoding':'gzip, deflate',
         'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)like Gecko',
         'Host':'jwxt.ecjtu.jx.cn',
}

app  =  flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/API/ClassQuery',methods=['POST'])
def getClassJsonData():

	username = flask.request.form["username"]
	password = flask.request.form["password"]
	year = flask.request.form["year"]
	term = flask.request.form["term"]

	loginRequest.request(username,password,headers)

	classInfoList = ClassAPI.getClassInfo(year,term)

	return jsonData.successData(classInfoList)

@app.route('/API/ExamQuery',methods=['POST'])
def getExamJsonData():

	username = flask.request.form["username"]
	password = flask.request.form["password"]
	year = flask.request.form["year"]
	term = flask.request.form["term"]

	loginRequest.request(username,password,headers)

	scoreInfoList = ExamAPI.getExamInfo(year,term,username)

	return jsonData.successData(scoreInfoList)

@app.route('/API/ScoreQuery',methods=['POST'])
def getScoreJsonData():

	username = flask.request.form["username"]
	password = flask.request.form["password"]
	year = flask.request.form["year"]
	term = flask.request.form["term"]

	loginRequest.request(username,password,headers)

	scoreInfoList = ScoreAPI.getScoreInfo(year,term)

	return jsonData.successData(scoreInfoList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=False, debug=True)
