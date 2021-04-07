from flask_wtf import FlaskForm
from wtforms import *

class AddPup(FlaskForm):

    owner_id = IntegerField("Owner's ID: ")
    puppy_name = StringField("Name: ")
    age = IntegerField("Age: ")
    gender = StringField("Gender: ")
    height_inches = DecimalField("Height (in): ", rounding = None)
    color = StringField("Color: ")
    favorite_food = StringField("Favorite Food: ")
    submit = SubmitField('Add')


class RemovePup(FlaskForm):

    puppy_id = IntegerField("Puppy's ID: ")
    puppy_name = StringField("Puppy's Name: ")


class AddOwner(FlaskForm):

    owner_name = StringField("Name: ")
    address = StringField("Address: ")
    city = StringField("City: ")
    state = StringField("State: ")
    zipcode = IntegerField("Zip Code: ")
    submit = SubmitField('Add')

