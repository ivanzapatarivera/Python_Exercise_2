import pandas as pd
import sqlalchemy as sql
from sqlalchemy import MetaData
from config import db_uri

engine = sql.create_engine(db_uri)

data_owner = pd.read_sql_table('owner', engine)
data_puppies = pd.read_sql_table('puppies', engine)


#####################
### OWNER QUERIES ###
#####################


# Setting dataframe for owner table
df_owner = pd.DataFrame(data_owner)

# Printing 'owner' table head for reference formatting data
data_owner['owner_name'] = data_owner['owner_name'].str.capitalize()
data_owner['address'] = data_owner['address'].str.title()
data_owner['city'] = data_owner['city'].str.title()
data_owner['state'] = data_owner['state'].str.upper()
print(data_owner.head()) # Printing results

# Querying the amount of records in table using Pandas' len(dataframe)
owner_count_rows = 'Number of records in \'owner\' table:  ' + str(len(df_owner))
print(owner_count_rows) # Printing count of rows

# Querying the amount of columns in table using Pandas' .count() by calling dataframe
owner_count_columns = 'Number of columns in \'owner\' table:  ' + str(df_owner.count(axis = 1)[0])
print(owner_count_columns) # Printing count of columns

# Querying the amount of owners by zipcode located in each state
owner_groupby_attribute = data_owner.groupby(['state']).size()
print(owner_groupby_attribute) # Printing count of owners by state, then by zipcode columns



#######################
### PUPPIES QUERIES ###
#######################

data_puppies['puppy_name'] = data_puppies['puppy_name'].str.title()
data_puppies['age'] = data_puppies['age'].astype(int)
data_puppies['favorite_food'] = data_puppies['favorite_food'].str.title()

# Setting dataframe for puppies table
df_puppies = pd.DataFrame(data_puppies)

# Printing 'owner' table head for reference
print(df_puppies.head())

# Querying the amount of records in table using Pandas' len(dataframe)
puppies_count_rows = 'Number of records in \'puppies\' table:  ' + str(len(df_puppies))
print(puppies_count_rows)

# Querying the amount of columns in table using Pandas' .count() by calling dataframe
puppies_count_columns = 'Number of columns in \'puppies\' table:  ' + str(df_puppies.count(axis = 1)[0])
print(puppies_count_columns)

# Querying the amount of puppies by color
df_puppies['age'] = df_puppies['age'].astype(int)
puppies_groupby_attribute = df_puppies.groupby(['color']).size()
print(puppies_groupby_attribute)