from sqlalchemy import Column, Integer, String

from app import db


class Category(db.Model):
	id = Column(Integer, primary_key)  
	name = Column(String(128), nullable=False, unique=True)
	desc = Column(String(256), nullable=True, unique=False)
	slug = Column(String(128), nullable=False, unique=True)
		