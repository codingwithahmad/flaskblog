from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from utils.forms import MultipleCheckBoxField


class PostForm(FlaskForm):
	title = StringField(validators=[DataRequired()])
	summery = TextAreaField()
	content = TextAreaField(validators=[DataRequired()])
	slug = StringField(validators=[DataRequired()])
	categories = MultipleCheckBoxField(coerce=int)


class CategoryForm(FlaskForm):
	name = StringField(validators=[DataRequired()])
	slug = StringField(validators=[DataRequired()])
	desc = TextAreaField()

class SearchForm(FlaskForm):
    search_query = StringField(validators=[DataRequired()])
