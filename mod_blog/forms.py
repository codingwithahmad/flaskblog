from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired
from utils.forms import MultipleCheckBoxField


class PostForm(FlaskForm):
	title = StringField(validators=[DataRequired()])
	summery = TextAreaField()
	content = TextAreaField(validators=[DataRequired()])
	slug = StringField(validators=[DataRequired()])
	categories = MultipleCheckBoxField()


class CategoryForm(FlaskForm):
	name = StringField(validators=[DataRequired()])
	slug = StringField(validators=[DataRequired()])
	desc = TextAreaField()
