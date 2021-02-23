#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, redirect, request, session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import sys, os, time, datetime
import json

app = Flask(__name__)
app.secret_key = '087fahvaln'

login_manager = LoginManager()
login_manager.init_app(app)

DATAFILE = "./data/msg.json"

class User(UserMixin):
	def __init__(self, user_id, name, password):
		self.user_id = user_id
		self.name = name
		self.password = password
	def get_id(self):
		return self.user_id

ken = User(0,"ken", "aaa")
mai = User(1, "mai", "bbb")
users = [ken, mai]

# json_card = [{ "usr":"", "time":"", "msg": ""}]

@login_manager.user_loader
def load_user(user_id):
	return users[user_id]

@login_manager.unauthorized_handler
def unauthorized():
	return redirect('/login')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login', methods=['GET','POST'])
def try_login():

	if "name" in request.form:
		name = request.form["name"]
	if "password" in request.form:
		password = request.form["password"]

	if (name == None) or (password == None):
		return redirect('/login')
	
	user_id = -1

	for user in users:
		if user.name == name and user.password == password:
			user_id = user.get_id()
	if user_id <= -1:
		return redirect('/login')

	user = User(user_id, name, password)
	login_user(user)

	return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
	json_card = []
	if os.path.exists(DATAFILE):
		with open(DATAFILE, 'r') as f:
			json_card = json.load(f)
	return render_template('index.html', cards=json_card)

@app.route('/write', methods=['POST'])
@login_required
def write():
	json_card = []
	if os.path.exists(DATAFILE):
		with open(DATAFILE, 'r') as f:
			json_card = json.load(f)
	# app.logger.debug(str(current_user.name))
	if 'msg' in request.form:
		msg = request.form["msg"].encode('utf-8')
		t = str(datetime.datetime.fromtimestamp(time.time()))
		u = current_user.name.encode('utf-8')
		json_card.insert(0, {"msg":msg, "time":t, "usr":u})
		with open(DATAFILE, 'w') as f:
			json.dump(json_card, f)
	return redirect('/')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')