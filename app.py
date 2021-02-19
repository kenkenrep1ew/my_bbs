from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/try_login')
def try_login():
	return "try_login"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/write')
def write():
	return "Index.html from /write"

@app.route('/logout')
def logout():
	return "Log out!!"


if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')