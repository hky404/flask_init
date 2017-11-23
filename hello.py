from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			return "Welcome back, {}".format(request.form['username'])
		else:
			error = 'Incorrect username and password'
	return render_template('login.html', error_var=error)

def valid_login(username, password):
	if username == password:
		return True
	else:
		return False


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name_var=name)  # variable 'name_var' is used in the html template


if __name__ == '__main__':
    app.debug = True
    app.run()
