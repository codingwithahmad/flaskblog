from flask import session, render_template, request, abort
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin

@admin.route('/')
def index():
	return "Hello from admin Index"


@admin.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		if not form.validate_on_submit():
			abort(400)
		user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
		if not user:
			return "Incorrect Credentials", 400			
	return render_template("admin/login.html", form=form)