from flask import Falsk
from flask import url_for,redirect
from app import app

@app.route('/')
def index() :
	return 'ok'
