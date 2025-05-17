import pandas as pd
import pymysql
from pymongo import MongoClient

# MySQL connection
mysql_conn = pymysql.connect(
    host="localhost", user="root", password="yourpass", database="legacy_db"
)
df = pd.read_sql("SELECT * FROM users", mysql_conn)

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_col = mongo_client["hybrid_db"]["users"]

# Insert into MongoDB
mongo_col.insert_many(df.to_dict(orient="records"))
print("✅ Data migrated successfully.")
