from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

class AddPup(FlaskForm):

    name = StringField('Puppy\'s name: ')
    nickname = StringField('Puppy\'s nickname:')
    height_in_inches = StringField('Height (in): ')
    color = StringField('Furr color: ')
    favorite_food = ('Favorite food: ')
    submit = SubmitField('Add Puppy')

class DelPup(FlaskForm):

    id = IntegerField('Puppy\'s ID:')
    submit = SubmitField('Remove puppy')
