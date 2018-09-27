from app import app

@app.route('/')
def index() :
	return '这里是一个主页'
