from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	email = EmailField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):

	full_name = StringField()

	email = EmailField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	password_confirm = PasswordField(validators=[DataRequired()])