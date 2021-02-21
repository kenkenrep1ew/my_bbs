from flask import Flask, render_template, url_for, redirect, request
import sys

app = Flask(__name__)

msg ="test"
#グローバル変数では使えないので、ファイルに変える！！

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login')
def try_login():
	return redirect(url_for('index'))

@app.route('/')
def index():
	app.logger.debug("index")
	app.logger.debug(msg)
	return render_template('index.html', msg=msg)

@app.route('/write', methods=['POST'])
def write():
	if request.form["msg"] is not None:
		msg = request.form["msg"]
	app.logger.debug("write")
	app.logger.debug(msg)
	return redirect('/')

@app.route('/logout')
def logout():
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')