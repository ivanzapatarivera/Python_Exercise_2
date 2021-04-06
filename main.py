import os

# from forms import AddPuppy, DelPuppy, AddOwner, DelOwner
from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.exc import NoSuchTableError
from forms import AddPup


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


# class Owner(db.Model):

#     __tablename__ = 'owner'

#     owner_id = db.Column(db.Integer, primary_key = True)
#     owner_name = db.Column(db.Text)


#     def __init__(self, owner_name):
#         self.owner_name = owner_name
    

#     def __repr__(self):
#         return f"The owner's name is {self.owner_name}."

    # owner_id = db.Column(db.Integer, primary_key = True)
    # name = db.Column(db.Text)
    # address = db.Column(db.Text)
    # city = db.Column(db.Text)
    # state = db.Column(db.Text)
    # zipcode = db.Column(db.Numeric(5,0))

    # def __init__(self, owner_id, name, address, city, state, zipcode):
    #     self.owner_id = owner_id
    #     self.name = name
    #     self.address = address
    #     self.city = city
    #     self.state = state
    #     self.zipcode = zipcode


class Puppy(db.Model):
    
    __tablename__ = 'puppies'
    
    puppy_id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer)
    puppy_name = db.Column(db.Text)
    age = db.Column(db.Numeric(2,0))
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

    # nickname = db.Column(db.Text)
    # height_in_inches = db.Column(db.Numeric(2,1))
    # color = db.Column(db.Text)
    # favorite_food = db.Column(db.Text)
    # owner = db.Column(db.Text)

    # def __init__(self, puppy_id, owner_id, name, nickname, height_in_inches, color, favorite_food, owner):
    #     self.puppy_id = puppy_id
    #     self.owner_id = owner_id
    #     self.name = name
    #     self.nickname = nickname
    #     self.height_in_inches = height_in_inches
    #     self.color = color
    #     self.favorite_food = favorite_food
    #     self.owner = owner

    # def __repr__(self):
    #     return f'Puppy\'s name is {self.name}. \n And has been adopted by {self.owner}. \n S/he loves {self.favorite_food} and likes to be called by {self.nickname}! \n \n Here are some facts! \n ID: {self.puppy_id} \n Furr Color: {self.color} \n Height (in): {self.height_in_inches}'


# Query to select all data from table puppies and force an error to create tables if needed
sql = 'SELECT * FROM puppies'
engine = create_engine(db_uri)
session = db.session()

# Validating if sql string will throw a try/except error
# If it throws an error, .create_all() method will execute
try: 
    cursor = session.execute(sql).cursor
    if(cursor):
        print('CONNECTED')
        db.create_all()
except:
    print(f'Table does not exist and string {sql} was not executed.')
    print(f'*** CREATING TABLE ***')
    db.create_all()
    print(f'*** TABLE CREATED ***')



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_pup', methods=['GET','POST'])
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

        return redirect(url_for('index'))

    return render_template('add.html', form = form)



if __name__ == "__main__":
    app.run(debug = True)