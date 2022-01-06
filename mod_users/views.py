from flask import request, render_template

from . import users
from .forms import RegisterForm

@users.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST':
		if not form.validate_on_submit():
			return render_template('users/register.html', form=form)
		else:
			pass
			

	return render_template('users/register.html', form=form)
