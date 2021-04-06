import os

# from forms import AddPuppy, DelPuppy, AddOwner, DelOwner
from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.exc import NoSuchTableError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

### MySQL DATABASE SECTION ###
import config
from config import username, password, server, database, db_uri

# basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

## Defining db
db = SQLAlchemy(app)
Migrate(app,db)


class Owner(db.Model):

    __tablename__ = 'owner'

    owner_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zipcode = db.Column(db.Numeric(5,0))

    def __init__(self, owner_id, name, address, city, state, zipcode):
        self.owner_id = owner_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode


class Puppy(db.Model):
    
    __tablename__ = 'puppies'
    
    puppy_id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey(Owner.owner_id), nullable = False)
    name = db.Column(db.Text)
    nickname = db.Column(db.Text)
    height_in_inches = db.Column(db.Numeric(2,1))
    color = db.Column(db.Text)
    favorite_food = db.Column(db.Text)

    def __init__(self, puppy_id, name, nickname, height_in_inches, color, owner, favorite_food):
        self.puppy_id = puppy_id
        self.name = name
        self.nickname = nickname
        self.height_in_inches = height_in_inches
        self.color = color
        self.owner = owner
        self.favorite_food = favorite_food


# Query to select all data from table puppies
sql = 'SELECT * FROM puppies'

# Creating MySQL engine
engine = create_engine(db_uri)

# Opening a session to throw try/except error
session = db.session()

# Validating if sql string will throw a try/except error
# If it throws an error, .create_all() method will execute
try: 
    cursor = session.execute(sql).cursor
    if(cursor):
        print('connected')
    else: 
        print('table does not exist')
except:
    db.create_all()


