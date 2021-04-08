import pandas as pd
import sqlalchemy as sql
from sqlalchemy import MetaData
from config import db_uri

engine = sql.create_engine(db_uri)


# Dataframes for tables in db
df_data_owner = pd.read_sql_table('owner', engine)
df_data_puppies = pd.read_sql_table('puppies', engine)


#####################
### OWNER QUERIES ###
#####################


# Printing 'owner' table head for reference formatting data
df_data_owner['owner_name'] = df_data_owner['owner_name'].str.capitalize()
df_data_owner['address'] = df_data_owner['address'].str.title()
df_data_owner['city'] = df_data_owner['city'].str.title()
df_data_owner['state'] = df_data_owner['state'].str.upper()
print(df_data_owner.head()) # Printing results

# Querying the amount of records in table using Pandas' len(dataframe)
owner_count_rows = 'Number of records in \'owner\' table:  ' + str(len(df_data_owner))
print(owner_count_rows) # Printing count of rows

# Querying the amount of columns in table using Pandas' .count() by calling dataframe
owner_count_columns = 'Number of columns in \'owner\' table:  ' + str(df_data_owner.count(axis = 1)[0])
print(owner_count_columns) # Printing count of columns

# Querying the amount of owners by zipcode located in each state
owner_groupby_attribute = df_data_owner.groupby(['state']).size()
print(owner_groupby_attribute) # Printing count of owners by state, then by zipcode columns



#######################
### PUPPIES QUERIES ###
#######################

df_data_puppies['puppy_name'] = df_data_puppies['puppy_name'].str.title()
df_data_puppies['age'] = df_data_puppies['age'].astype(int)
df_data_puppies['favorite_food'] = df_data_puppies['favorite_food'].str.title()

# Printing 'owner' table head for reference
print(df_data_puppies.head())
print('***************')
print(df_data_puppies)

# Querying the amount of records in table using Pandas' len(dataframe)
puppies_count_rows = 'Number of records in \'puppies\' table:  ' + str(len(df_data_puppies))
print(puppies_count_rows)

# Querying the amount of columns in table using Pandas' .count() by calling dataframe
puppies_count_columns = 'Number of columns in \'puppies\' table:  ' + str(df_data_puppies.count(axis = 1)[0])
print(puppies_count_columns)

# Querying the amount of puppies by color
df_data_puppies['age'] = df_data_puppies['age'].astype(int)
puppies_groupby_attribute = df_data_puppies.groupby(['color']).size()
print(puppies_groupby_attribute)