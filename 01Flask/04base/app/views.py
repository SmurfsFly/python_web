from app import app
from flask import render_template,redirect
from flask import url_for
@app.route('/index')
def index() :
	return redirect(url_for('.classp'))
	return render_template('index.html')
@app.route('/class')
def classp() :
	return render_template('classphoto.html')
app.run(debug=True)

