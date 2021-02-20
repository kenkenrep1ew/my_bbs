from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login')
def try_login():
	return redirect(url_for('index'))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/write')
def write():
	return redirect(url_for('index'))

@app.route('/logout')
def logout():
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')