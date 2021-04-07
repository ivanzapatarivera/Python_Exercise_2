import pandas as pd
import sqlalchemy as sql
from config import db_uri


# Creating engine to connect to db_uri (MySQL)
engine = sql.create_engine(db_uri)

# Calling and reading local CSV file
# owner_filename = 'owner_batch.csv'
# data = pd.read_csv(owner_filename)

# # Defining dataframe (df) with Pandas
# df = pd.DataFrame(data, columns = ['owner_id', 'owner_name', 'address', 'city', 'state', 'zipcode'])

# # Releasing BATCH to MySQL
# df.to_sql(con = engine, name = 'owner', if_exists='append', index = False)


# Validating all records were inserted successfully
query = "SELECT * FROM owner"
df_query = pd.read_sql_query(query, engine)
print('** CONNECTED **')
print(df_query)
print('***************')

# query2 = "INSERT INTO owner (owner_name, address, city, state, zipcode) VALUES (%s, %s, %s, %s, %s)"
# owner_filename = 'owner_batch.csv'
# data = pd.read_csv(owner_filename)
# df2 = pd.DataFrame(data, columns = ['owner_id', 'owner_name', 'address', 'city', 'state', 'zipcode'])
# df3 = pd.read_sql_query(query2, engine)


# print('***************')
# print(df1)
# print('***************')
