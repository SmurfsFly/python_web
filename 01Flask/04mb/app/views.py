from app import app
from flask import render_template

@app.route('/base')
def base() :
	return render_template('base.html')
