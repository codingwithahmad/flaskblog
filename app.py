from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
	return 'Blog Home, Welcome!'


from mod_admin import admin
app.register_blueprint(admin)

