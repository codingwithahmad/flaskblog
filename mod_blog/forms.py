from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
	title = StringField(validators=[DataRequired()])
	summery = TextAreaField()
	content = TextAreaField(validators=[DataRequired()])
	slug = StringField(validators=[DataRequired()])





class CategoryForm(FlaskForm):
	name = StringField(validators=[DataRequired()])
	slug = StringField(validators=[DataRequired()])
	desc = TextAreaField()