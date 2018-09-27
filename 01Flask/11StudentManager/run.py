from app import app
import pymysql
pymysql.install_as_MySQLdb()
from app import db
from app.models import Student,Teacher

db.create_all()

app.run()
