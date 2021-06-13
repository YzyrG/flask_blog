# blog.py - controller

from flask import Flask, render_template, request, session, flash,\
	redirect, url_for, g

import sqlite3

# configuration
DATABASE = "blog.db"

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#view:login.html
@app.route('/')
def login() :
	return render_template('login.html')

# view:main.html
@app.route('/mian')
def main():
	return render_template('main.html')
	

if __name__ == '__main__':
	app.run(debug=True) 

