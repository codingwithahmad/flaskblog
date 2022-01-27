from flask import (abort, flash, redirect, render_template, request, session,
                   url_for)
from sqlalchemy.exc import IntegrityError

from app import db
from mod_blog.forms import CreatePostForm, ModifyPostForm
from mod_blog.models import Post
from mod_users.forms import LoginForm, RegisterForm
from mod_users.models import User

from . import admin
from .utils import admin_only


@admin.route('/')
@admin_only
def index():
	return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		if not form.validate_on_submit():
			abort(400)
		user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
		if not user:
			flash("Incorrect Credentials", category="error")
			return render_template("admin/login.html", form=form)
		if not user.check_password(form.password.data):
			flash("Incorrect Credentials", category="error")
			return render_template("admin/login.html", form=form)
		if not user.is_admin():
			flash("You don't have permission to access admin panel", category="error")
			return render_template("admin/login.html", form=form)
		
		session['email'] = user.email
		session['user_id'] = user.id
		session['role'] = user.role

		return redirect(url_for('admin.index'))

	if session.get('role') == 1:
		return redirect(url_for('admin.index'))

	return render_template("admin/login.html", form=form)


@admin.route('/logout/', methods=['GET'])
@admin_only
def logout():
	session.clear()
	flash('You logged out successfully', 'success')
	return redirect(url_for('admin.login'))

@admin.route('/users/', methods=['GET'])
@admin_only
def list_users():
	users = User.query.order_by(User.id.desc()).all()

	return render_template('admin/list_users.html', users=users)


@admin.route('/users/new/', methods=['GET'])
@admin_only
def get_create_user():
	form = RegisterForm()
	return render_template('admin/create_user.html', form=form)

@admin.route('/users/new/', methods=['POST'])
@admin_only
def post_create_user():
	form = RegisterForm(request.form)
	if not form.validate_on_submit():
			return render_template('admin/create_user.html', form=form)
	if not form.password.data == form.password_confirm.data:
		error_message = "Password and Confirm Password dosn't match"
		form.password.errors.append(error_message)
		form.password_confirm.errors.append(error_message)

		return render_template('admin/create_user.html', form=form)


	new_user = User()
	new_user.full_name = form.full_name.data
	new_user.email = form.email.data
	new_user.set_password(form.password.data)
	try:
		db.session.add(new_user)
		db.session.commit()
		flash(f'User {new_user.username} create successfully', 'success')
	except IntegrityError:
		db.session.rollback()
		form.email.errors.append('This email is registered, please use another email')
	
	return render_template('admin/create_user.html', form=form)

@admin.route('/posts/new/', methods=['GET', 'POST'])
@admin_only
def create_post():
	form = CreatePostForm(request.form)
	if request.method == 'POST':
		if not form.validate_on_submit():
			return "1"


		new_post = Post()

		new_post.title = form.title.data
		new_post.content = form.content.data
		new_post.summery = form.summery.data
		new_post.slug = form.slug.data

		try:
			db.session.add(new_post)
			db.session.commit()
			flash('Post created', 'success')
			return redirect(url_for('admin.index'))
		except IntegrityError:
			db.session.rollback()
			flash('Slug Duplicated')
			

	return render_template('admin/create_post.html', form=form)


@admin.route('/posts/', methods=['GET'])
@admin_only
def list_posts():
	posts = Post.query.order_by(Post.id.desc()).all()
	return render_template('admin/list_posts.html', posts=posts)

@admin.route('/posts/delete/<int:post_id>/', methods=['GET'])
@admin_only
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	db.session.delete(post)
	db.session.commit()
	flash(f"{post.title} delete successfully")
	return redirect(url_for('admin.list_posts'))

@admin.route('/posts/modify/<int:post_id>/', methods=['GET', 'POST'])
@admin_only
def modify_post(post_id):
	post = Post.query.get_or_404(post_id)
	form = ModifyPostForm(obj=post)
	if request.method == 'POST':
		if not form.validate_on_submit():
			return render_template('admin/modify_post.html', data={'form': form, 'post': post })
		
		post.title = form.title.data
		post.content = form.content.data
		post.summery = form.summery.data
		post.slug = form.slug.data

		try:
			db.session.commit()
			flash(f'{post.title} is modified!')
		except IntegrityError:
			db.session.rollback()
			flash('Slug Duplicated')
		

	return render_template('admin/modify_post.html', data={'form': form, 'post': post })
