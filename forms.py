from flask_wtf import FlaskForm
from wtforms import *

class AddPup(FlaskForm):

    # owner_id = form.owner_id.data
    #     puppy_name = form.puppy_name.data
    #     age = form.age.data
    #     gender = form.gender.data
    #     height_inches = form.height_inches.data
    #     color = form.color.data
    #     favorite_food = form.favorite_food.data

    owner_id = IntegerField("Owner's ID: ")
    puppy_name = StringField("Name: ")
    age = IntegerField("Age: ")
    gender = StringField("Gender: ")
    height_inches = DecimalField("Height (in): ", rounding = None)
    color = StringField("Color: ")
    favorite_food = StringField("Favorite Food: ")
    submit = SubmitField('Add')


