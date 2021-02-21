from flask import Flask, render_template, url_for, redirect, request
import sys, os, time, datetime
import json

app = Flask(__name__)

DATAFILE = "./data/msg.json"

# json_card = { "usr":"", "time":"", "msg": ""}

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login')
def try_login():
	return redirect(url_for('index'))

@app.route('/')
def index():
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