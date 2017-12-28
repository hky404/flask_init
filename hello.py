from flask import Flask, request, render_template, redirect, url_for, flash, make_response

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Succesfully logged in")
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', request.form.get('username'))
            return response
        else:
            error = 'Incorrect username and password'
    return render_template('login.html', error_var=error)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username_var=username)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKeyxyz'
    app.run()
