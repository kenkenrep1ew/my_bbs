from flask import Flask, render_template, url_for, redirect, request
import sys, os

app = Flask(__name__)

DATAFILE = "./data/msg.txt"

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login')
def try_login():
	return redirect(url_for('index'))

@app.route('/')
def index():
	msg = ""
	if os.path.exists(DATAFILE):
		with open(DATAFILE, 'rt') as f:
			msg = f.read()

	# app.logger.debug("index")
	# app.logger.debug(msg)
	return render_template('index.html', msg=msg)

@app.route('/write', methods=['POST'])
def write():
	if 'msg' in request.form:
		msg = str(request.form["msg"])
		with open(DATAFILE, 'a') as f:
			f.write(msg)
	# app.logger.debug("write")
	# app.logger.debug(msg)
	return redirect('/')

@app.route('/logout')
def logout():
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')