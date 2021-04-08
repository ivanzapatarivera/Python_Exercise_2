import pandas as pd
import pandas.io.formats.style 
import numpy as np
import sqlalchemy as sql
from config import db_uri

engine = sql.create_engine(db_uri)

df_owners = pd.read_sql_table('owner', engine)
df_puppies = pd.read_sql_table('puppies', engine)

# Renaming columns for owners dataframe
df_owners = df_owners.rename(columns= { "owner_id": "Owner ID", "owner_name": "Owner Name", "address": "Address", "city": "City", "state": "State", "zipcode": "Zip Code" })
df_puppies = df_puppies.rename(columns= { "puppy_id": "Puppy ID", "owner_id": "Owner ID", "puppy_name": "Puppy Name", "age": "Age", "gender": "Gender", "height_inches": "Height (in)", "color": "Color", "favorite_food": "Favorite Food" })


# Capitalizing names in owner table results
df_owners['Owner Name'] = df_owners['Owner Name'].str.capitalize()
df_owners['Address'] = df_owners['Address'].str.title()
df_owners['City'] = df_owners['City'].str.title()
df_owners['State'] = df_owners['State'].str.upper()


# Capitalizing names in puppies table results
df_puppies['Puppy Name'] = df_puppies['Puppy Name'].str.capitalize()
df_puppies['Favorite Food'] = df_puppies['Favorite Food'].str.title()

print(df_owners.head(2))
print(df_puppies)


# Querying the amount of owners and puppies registered
amount_owners = len(df_owners)
amount_puppies = len(df_puppies)
print('Amount of owners registered: ' + str(amount_owners) + '\nAmount of puppies registered: ' + str(amount_puppies))


# Querying amount of columns in tables
amount_cols_owners = df_owners.count(axis = 1)[0]
amount_cols_pupppies = df_puppies.count(axis = 1)[0]
print('Amount of columns in owner table : ' + str(amount_cols_owners) + '\nAmount of columns in puppies table: ' + str(amount_cols_pupppies))


# Organizing new dataframe with owner id's and puppy names
df_owner_id_in_puppies = pd.DataFrame(df_puppies['Owner ID'])
df_owner_names = pd.DataFrame(df_owners[['Owner ID', 'Owner Name']])

df_joined_table = df_owner_names.merge(df_owner_id_in_puppies, how = 'left') # 'join left' of new datafrmes


puppies_per_owner = ((df_joined_table.groupby(['Owner Name']).size()).reset_index(name = 'Total Puppies')).sort_values(by = ['Total Puppies'], ascending = False)
puppies_per_owner = puppies_per_owner.reset_index().drop(['index'], axis = 1)
print(puppies_per_owner) 


# Obtaining sorted amount of favorite food by ranking
df_puppies = df_puppies.rename(columns = {'Favorite Food': 'Top Favorite Foods'})
favorite_food = ((df_puppies.groupby(['Top Favorite Foods']).size()).reset_index(name = 'Totals')).sort_values(by = ['Totals'], ascending = False)
favorite_food = favorite_food.reset_index().drop(['index'], axis = 1)
print(favorite_food)

# Obtaining sorted amount of puppies by color
puppies_color = ((df_puppies.groupby(['Color']).size()).reset_index(name = 'Totals')).sort_values(by = ['Totals'], ascending = False)
puppies_color = puppies_color.reset_index().drop(['index'], axis = 1)
print(puppies_color)


# Obtaining amount of puppies by age on a single row
less_than_five = len(df_puppies[df_puppies['Age'].between(0, 4)])
between_five_and_ten = len(df_puppies[df_puppies['Age'].between(5, 10)])
more_than_ten = len(df_puppies[df_puppies['Age'] > 10])

# Creating dataframe to enclose puppies by age
puppies_age = {'Less than 5': [less_than_five], 'Between 5 and 10': [between_five_and_ten], 'More than 10': [more_than_ten]}
df_puppies_age = pd.DataFrame(puppies_age)

print(less_than_five)
print(between_five_and_ten)
print(more_than_ten)
print(df_puppies_age)