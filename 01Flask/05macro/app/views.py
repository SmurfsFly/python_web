from app import app
from flask import render_template
@app.route('/')
def index() :
	t1 = {'name':'zhangsan','age':20,'sex':1}
	t2 = {'name':'zhangsan','age':20,'sex':1}
	t3 = {'name':'zhangsan','age':20,'sex':1}
	t4 = {'name':'zhangsan','age':20,'sex':1}
	return render_template('index.html',slist=[t1,t2,t3,t4])
