from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			flash("Succesfully logged in")
			return redirect(url_for('welcome', username=request.form['username']))
		else:
			error = 'Incorrect username and password'
	return render_template('login.html', error_var=error)

def valid_login(username, password):
	if username == password:
		return True
	else:
		return False

@app.route('/welcome/<username>')
def welcome(username):
	return render_template('welcome.html', username_var=username)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKeyxyz'
    app.run()
