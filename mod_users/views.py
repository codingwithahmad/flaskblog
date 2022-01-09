from flask import request, render_template, flash

from . import users
from .forms import RegisterForm
from app import db
from .models import User

@users.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST':
		if not form.validate_on_submit():
			return render_template('users/register.html', form=form)
		if not form.password.data == form.password_confirm.data:
			error_message = "Password and Confirm Password dosn't match"
			form.password.errors.append(error_message)
			form.password_confirm.errors.append(error_message)

			return render_template('users/register.html', form=form)

		user = User.query.filter(User.email==form.email.data).first()

		if user is None:
			new_user = User()
			new_user.full_name = form.full_name.data
			new_user.email = form.email.data
			new_user.set_password(form.password.data)

			db.session.add(new_user)
			db.session.commit()

			flash('You create your account successfully', 'success')



		else:
			form.email.errors.append('This email is registered, please use another email')
			return render_template('users/register.html', form=form)			

	return render_template('users/register.html', form=form)
