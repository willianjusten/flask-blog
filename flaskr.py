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