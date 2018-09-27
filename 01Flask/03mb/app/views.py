from app import app
from flask import render_template
@app.route('/')
def index():
	return render_template('index.html',a='其',b='x')

@app.route('/a')
def a() :
	return render_template('index.html',a="蓝精灵",b="小仙女")

@app.route('/student')
def student() :
	s_list=['张三','李四']
	return render_template('student.html',slist=s_list)
@app.route('/teacher')
def teacher() :
	t_dic = {'name':'zhangsan','age':35,'sex':1}
	return render_template('teacher.html',t=t_dic)
@app.route('/teachers')
def teachers() :
	t1 = {'name':'zhangsan','age':35,'sex':1}
	t2 = {'name':'zhangsan','age':35,'sex':1}
	t3 = {'name':'zhangsan','age':35,'sex':1}
	t4 = {'name':'zhangsan','age':35,'sex':1}
	t_list = [t1,t2,t3,t4]
	return render_template('teachers.html',tlist=t_list)
