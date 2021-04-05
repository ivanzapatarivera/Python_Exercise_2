import os

# from forms import AddPuppy, DelPuppy, AddOwner, DelOwner
from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

### MySQL DATABASE SECTION ###
import config
from config import username, password, server, db

# basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{server}/{db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

## Defining db
db = SQLAlchemy(app)
Migrate(app,db)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

if __name__ == "__main__":
    app.run(debug=True)