from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	email = EmailField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
