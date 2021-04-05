import os

# from forms import AddPuppy, DelPuppy, AddOwner, DelOwner
from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

### MySQL DATABASE SECTION ###
import config
from config import username, password

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@server/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## Defining db
db = SQLAlchemy(app)
Migrate(app,db)