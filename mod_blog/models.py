from sqlalchemy import Column, Integer, String, Text, Table, Foreign_key

from app import db


posts_categories = Table('posts_categories', db.metadata,
	Column('post_id', Integer, Foreign_key('posts.id')),
	Column('category_id', Integer, Foreign_key('categories.id'))
)



class Category(db.Model):
	__tablename__ = "categories"
	id = Column(Integer, primary_key=True)  
	name = Column(String(128), nullable=False, unique=True)
	desc = Column(String(256), nullable=True, unique=False)
	slug = Column(String(128), nullable=False, unique=True)

class Post(db.Model):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True)  
	title = Column(String(128), nullable=False, unique=True)
	summery = Column(String(256), nullable=True, unique=False)
	content = Column(Text, nullable=False, unique=False)
	slug = Column(String(128), nullable=False, unique=True)
		