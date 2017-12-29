from flask import Flask, request, render_template, redirect, url_for, flash, session

app = Flask(__name__)

import logging
from logging.handlers import RotatingFileHandler


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Succesfully logged in")
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username and password'
            app.logger.warning("Incorrect username and password for user ({})".format(request.form.get('username')))
    return render_template('login.html', error_var=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username_var=session['username'])
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = '\xa1!Y\xd3\xe3\xf2\x1c\xad\xa8\x1ad\xb1U\xb11k\xce\xc9\xe0t\xde\xfe\x9f\x9d'

    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    
    app.run()
