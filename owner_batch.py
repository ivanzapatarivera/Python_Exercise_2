import pandas as pd
import sqlalchemy as sql
from config import db_uri


# Creating engine to connect to db_uri (MySQL)
engine = sql.create_engine(db_uri)

# Calling and reading local CSV file
owner_filename = 'owner_batch.csv'
data = pd.read_csv(owner_filename)
print(data) # Validating file exists

# Defining dataframe (df) with Pandas
df = pd.DataFrame(data, columns = ['owner_id', 'owner_name', 'address', 'city', 'state', 'zipcode'])
df.to_sql(con = engine, name = 'owner', if_exists='append', index = False) # Releasing BATCH to MySQL


# Validating all records were inserted successfully
query = "SELECT * FROM owner"
df_query = pd.read_sql_query(query, engine)
print('** CONNECTED **')
print(df_query)
print('***************')