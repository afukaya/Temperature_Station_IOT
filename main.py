from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer(), primary_key=True)
    username = db.Column('username', db.String(255))
    password = db.Column('password', db.String(255))

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return f'<User: {self.username}>'

@app.route('/')
def home():
    return '<h1>Hello World</h1>'

if __name__ == '__main__' :
    app.run()