import pymysql
pymysql.install_as_MySQLdb()#python3默认不可以使用MySQLdb
from app import db
from app.models import Student,BTeacher
db.create_all()
