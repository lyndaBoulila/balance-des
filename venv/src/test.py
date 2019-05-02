import pandas as pd
from pymongo import MongoClient

#  envoyer les données vers mongo db
# inserting data in MongoDB

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database
db = conn.datbasetest

# Created or Switched to collection names: my_gfg_collection
collection = db.Tweets
cursor = collection.find()
table1=pd.DataFrame(cursor)
table2=pd.DataFrame(table1["user"])
liste = table2.to_dict()
liste2 = liste["user"]
liste3=liste2.values ()
table4= pd.DataFrame(liste3)
print (table4.columns)



