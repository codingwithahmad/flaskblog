from flask import session, render_template, request
from mod_users.forms import LoginForm
from . import admin

@admin.route('/')
def index():
	return "Hello from admin Index"


@admin.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		pass
	return render_template("admin/login.html", form=form)