from flask import session
from . import admin

@admin.route('/')
def index():
	return "Hello from admin Index"


@admin.route('/login')
def login():
	return "1"