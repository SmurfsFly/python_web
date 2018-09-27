from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,BooleanField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import EqualTo
class RegisterForm(FlaskForm) :
	name = StringField(label='名字', validators=[DataRequired(), Length(1,64)])
	email = StringField(label='邮箱', validators=[DataRequired(), Length(1,128), Email('邮箱好像不对')])
	password = PasswordField(label='密码', validators=[DataRequired(), Length(6,128)])
	password_again = PasswordField(label='密码')
	submit = SubmitField(label='提交')
