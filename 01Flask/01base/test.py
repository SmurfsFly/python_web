#1.导入flask
from flask import Flask
from flask import request
#2.构建flask对象
#flask对象socket，能与所有的浏览器建立连接
#能够接收浏览器数据，并发送数据给浏览器
#浏览器和web服务器之间的数据符合http协议
#flask对象能够解决http协议
app = Flask(__name__)
#3.定义视图函数并添加路由

@app.route('/abc')
def index() :
	return 'hello flask'

@app.route('/')
def root() :
	return '''
		<h1>hello 蓝精灵</h1>
'''

#如何让渲染前端工程师写好的页面
#a.在test.py中的同级目录下创建templates和static文件夹
#b.把*.html文件放到templates下文件夹
#c.把 其他文件 放到static下文件夹
#d.构建一个视图函数并且添加一个路由
#e.替换css js images的途径

#:把css/ 替换成/static/css/
#:%s/css\//\/static\/css\//g

#构建一个视图函数并添加一个路由
from flask import render_template #导入内容读出字符串
@app.route('/bp')
def bp() :
	#把index.html的内容读出做成字符串，然后返回 发送给浏览器
	#注意：render_template默认去templates找文件
 	return render_template('index.html')

#127.0.0.1:5000/add/4/5
#动态路由变量的三种类型:int float path
@app.route('/add/<int:a>/<int:b>')
def add(a,b) :
	return str(a + b)

#静态路由优先
@app.route('/add/<int:a>/<int:b>')
	
def hello() :
	return 'hello'
#4.运行flask
#app.run(debug=True)
app.run(host='0.0.0.0',port=5000,debug=True)
