from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return "User {}".format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id must be an integer
	return "Post {}".format(post_id)

@app.route('/hello')
def hello_world():
	return 'Hello Everyone!!'

if __name__ == '__main__':
	app.debug = True
	app.run()