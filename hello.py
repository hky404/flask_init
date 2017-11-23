from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return 'Username is {}'.format(request.values['username'])
    else:
        return '<form method="get" action="/login"><input type="text" name="username"><p><button type="submit">Submit</button></p></form>'


if __name__ == '__main__':
    app.debug = True
    app.run()
