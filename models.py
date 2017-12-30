from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'user'
	user_id = db.Column('user_id', db.Integer, primary_key=True)
	username = db.Column('username', db.Unicode)
	password = db.Column('password', db.Unicode)