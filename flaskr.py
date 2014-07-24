# imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# create application
app = Flask(__name__)
app.config.from_object(__name__)

# load default config
app.config.update(dict(
	DATABASE = os.path.join(app.root_path, 'flaskr.db'),
	DEBUG = True,
	SECRET_KEY = os.urandom(24),
	USERNAME = 'admin',
	PASSWORD = 'default'
))
app.config.from_envvar('FLASK SETTINGS', silent=True)

def connect_db():
	"""Connects to the specific database"""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv 

def get_db():
	"""Opens  a new database connection if there is none yet for 
	the current application context
	"""
	if not hasattr(g, 'sqlite.db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db():
	"""Closes the database again at the end of the request"""
	if hasattr(g,'sqlite.db'):
		g.sqlite_db.close()

if __name__ == '__main__':
	app.run()