from flask import Flask, render_template, url_for, redirect, request, session
import sys, os, time, datetime
import json

app = Flask(__name__)
app.secret_key = '087fahvaln'

DATAFILE = "./data/msg.json"

USR = {"ken":"aaa", "mai":"bbb",}

# json_card = [{ "usr":"", "time":"", "msg": ""}]

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login', methods=['POST'])
def try_login():
	if "name" in request.form:
		name = request.form["name"]
	if "pw" in request.form:
		pw = request.form["pw"]
	if (name == None) or (pw == None):
		return redirect('/login')
	if check_login(name, pw) == False:
		return redirect('/login')
	else:
		return redirect(url_for('index'))

def check_login(name, pw):
	if not name in USR:
		return False
	if USR[name] != pw:
		return False
	else:
		session['login'] = name
		return True

def is_login():
	if 'login' in session:
		return True
	else:
		return False

@app.route('/')
def index():
	if not is_login():
		return redirect('/login')
	json_card = []
	if os.path.exists(DATAFILE):
		with open(DATAFILE, 'r') as f:
			json_card = json.load(f)

	# app.logger.debug("index")
	# app.logger.debug(msg)
	return render_template('index.html', cards=json_card)

@app.route('/write', methods=['POST'])
def write():
	json_card = []
	if os.path.exists(DATAFILE):
		with open(DATAFILE, 'r') as f:
			json_card = json.load(f)
	if 'msg' in request.form:
		msg = str(request.form["msg"])
		t = str(datetime.datetime.fromtimestamp(time.time()))
		u = ""
		json_card.append({"msg":msg, "time":t, "usr":u})
		with open(DATAFILE, 'w') as f:
			json.dump(json_card, f)
	# app.logger.debug("write")
	# app.logger.debug(msg)
	return redirect('/')

@app.route('/logout')
def logout():
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')