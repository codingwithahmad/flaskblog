from flask import render_template, request
from flask_sqlalchemy import get_debug_queries
from sqlalchemy import or_
from . import blog

from .models import Post

@blog.route('/')
def index():
	posts = Post.query.all()
	return render_template('blog/index.html', posts=posts)


@blog.route('/<string:slug>')
def single_post(slug):
	post = Post.query.filter(Post.slug==slug).first_or_404()
	return render_template('blog/single_post.html', post=post)


@blog.route('/search')
def search_blog():
    """
    domain.com/blog/search?q=Hello
    select from posts where title ilike '%Hello%'
    """

    search_query = request.args.get('q', '')

    title_cond = Post.title.ilike(f"%{search_query}%")
    summery_cond = Post.summery.ilike(f"%{search_query}%")
    content_cond = Post.content.ilike(f"%{search_query}%")
    found_posts = Post.query.filter(
        or_(
            title_cond,
            summery_cond,
            content_cond
        )
    ).all()
    return "Search"



