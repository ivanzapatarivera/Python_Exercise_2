import pandas as pd
import sqlalchemy as sql
from config import db_uri


# Creating engine to connect to db_uri (MySQL)
engine = sql.create_engine(db_uri)

# Calling and reading local CSV files with owner information 
owner_filename = 'owner_batch.csv'
data_owner = pd.read_csv(owner_filename)
print(data_owner) # Printing file data on console

# Defining dataframe (df) for Owner batch with Pandas
df_owner = pd.DataFrame(data_owner, columns = ['owner_name', 'address', 'city', 'state', 'zipcode'])
df_owner.to_sql(con = engine, name = 'owner', if_exists='append', index = False) # Releasing BATCH to MySQL



# Calling and reading local CSV files with puppies information
puppies_filename = 'puppies_batch.csv'
data_puppies = pd.read_csv(puppies_filename)
print(data_puppies) 

# Defining dataframe (df1) for Puppies batch with Pandas
df_puppies = pd.DataFrame(data_puppies, columns = ['owner_id', 'puppy_name', 'age', 'gender', 'height_inches', 'color', 'favorite_food'])
df_puppies.to_sql(con = engine, name = 'puppies', if_exists='append', index = False) 

# Validating all records were inserted successfully
query_owner = "SELECT * FROM owner"
query_puppies = "SELECT * FROM puppies"
df_query_owner = pd.read_sql_query(query_owner, engine)
df_query_puppies = pd.read_sql_query(query_puppies, engine)
print('** CONNECTED **')
print('**** OWNER ****')
print(df_query_owner)
print('*** PUPPIES ***')
print(df_query_puppies)
print('***************')