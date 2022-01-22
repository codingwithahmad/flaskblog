from flask import render_template

from . import blog

from .models import Post

@blog.route('/')
def index():
	posts = Post.query.all()
	return render_template('blog/index.html', posts=posts)
