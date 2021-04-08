import os

# from forms import AddPuppy, DelPuppy, AddOwner, DelOwner
from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.exc import NoSuchTableError
from forms import AddPup, RemovePup, AddOwner, RemoveOwner
import tkinter

# Importing tkinter for alert boxes on submit
from tkinter import messagebox


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

### MySQL DATABASE SECTION ###
import config

# Importing environmental variables using config.py
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
    owner_name = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zipcode = db.Column(db.Text)
    puppies = db.relationship('Puppy', lazy = 'select', backref = db.backref('pup', lazy='joined'))

    def __init__(self, owner_name, address, city, state, zipcode):
        self.owner_name = owner_name.lower()
        self.address = address.lower()
        self.city = city.lower()
        self.state = state.lower()
        self.zipcode = zipcode
    

    def __repr__(self):
        return f"The owner's name is {self.owner_name}."


class Puppy(db.Model):
    
    __tablename__ = 'puppies'
    
    puppy_id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, ForeignKey(Owner.owner_id, ondelete = 'CASCADE', onupdate = 'CASCADE'), nullable = False)
    puppy_name = db.Column(db.Text)
    age = db.Column(db.Numeric(2, asdecimal = False))
    gender = db.Column(db.Text)
    height_inches = db.Column(db.Numeric(precision = 3, scale = 1, asdecimal = True))
    color = db.Column(db.Text)
    favorite_food = db.Column(db.Text)

    def __init__(self, owner_id, puppy_name, age, gender, height_inches, color, favorite_food):
        self.owner_id = owner_id
        self.puppy_name = puppy_name.lower()
        self.age = age
        self.gender = gender.lower()
        self.height_inches = height_inches
        self.color = color.lower()
        self.favorite_food = favorite_food.lower()

    def __repr__(self):
        return f"{self.puppy_name}'s favorite food is {self.favorite_food}."


# Query to select all data from table puppies and force an error to create tables if needed
sql = 'SELECT * FROM puppies INNER JOIN owner'
engine = create_engine(db_uri)
session = db.session()

# Validating if sql string will throw a try/except error
# If it throws an error, .create_all() method will execute
try: 
    cursor = session.execute(sql).cursor
    if(cursor):
        print('CONNECTED')
       
except:
    print(f'Table does not exist and string {sql} was not executed.')
    print(f'*** CREATING TABLE ***')
    db.create_all()
    print(f'*** TABLE CREATED ***')



##############################################
###############    ROUTES    #################
##############################################


# Home Page
@app.route('/')
def index():
    return render_template('home.html')


# List of all registered owners and puppies 
@app.route('/list')
def list_pup():

    puppy_list = Puppy.query.all()
    owner_list = Owner.query.order_by(Owner.owner_name)
    return render_template('list.html', puppy_list = puppy_list, owner_list = owner_list)


# Add owner into database
@app.route('/add_owner', methods = ['GET', 'POST'])
def add_owner():

    form = AddOwner()

    if form.validate_on_submit():

        owner_name = form.owner_name.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        zipcode = form.zipcode.data
        added_owner = Owner(owner_name, address, city, state, zipcode)
        db.session.add(added_owner)
        db.session.commit()

        messagebox.showinfo('Confirmation', 'Owner has been added to PAWS.')
        return redirect(url_for('index'))
    
    return render_template('add_owner.html', form = form)


# Delete owner from database
@app.route('/del_owner', methods = ['GET', 'POST'])
def del_owner():

    form = RemoveOwner()

    if form.validate_on_submit():

        owner_id = form.owner_id.data
        this_owner = Puppy.query.get(owner_id)

        db.session.delete(this_owner)
        db.session.commit()

        return redirect(url_for('del_owner'))

    owner_list = Owner.query.order_by(Owner.owner_name)
    return render_template('del_owner.html', form = form, owner_list = owner_list)


# Add puppy into database
@app.route('/add_pup', methods = ['GET','POST'])
def add_pup():

    form = AddPup()
     

    if form.validate_on_submit():

        owner_id = form.owner_id.data
        puppy_name = form.puppy_name.data
        age = form.age.data
        gender = form.gender.data
        height_inches = form.height_inches.data
        color = form.color.data
        favorite_food = form.favorite_food.data

        added_puppy = Puppy(owner_id, puppy_name, age, gender, height_inches, color, favorite_food)
        db.session.add(added_puppy)
        db.session.commit()

        messagebox.showinfo('Confirmation', 'Puppy has been added to PAWS.')
        return redirect(url_for('list_pup'))
    
    gender_list = ['Female', 'Male', 'Non-binary', 'Unknown']
    owner_list = Owner.query.all()
    return render_template('add_puppy.html', form = form, owner_list = owner_list, gender_list = gender_list)


# Delete puppy from database
@app.route('/del_pup', methods = ['GET', 'POST'])
def del_pup():

    form = RemovePup()

    if form.validate_on_submit():

        puppy_id = form.puppy_id.data
        this_puppy = Puppy.query.get(puppy_id)

        db.session.delete(this_puppy)
        db.session.commit()



        return redirect(url_for('del_pup'))

    puppy_list = Puppy.query.all()
    owner_list = Owner.query.order_by(Owner.owner_name)
    return render_template('del_puppy.html', form = form, puppy_list = puppy_list, owner_list = owner_list)



if __name__ == "__main__":
    app.run(debug = True)