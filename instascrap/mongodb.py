from pymongo import MongoClient
import pandas as pd
import json
# pprint library is used to make the output look more pretty
from pprint import pprint
import gridfs
import pymongo

#Connect to MGDB data base
client=pymongo.MongoClient("mongodb://localhost:27017")
df=pd.read_csv("filtered_dataset.csv")
 

 #convert the data to json format
data=df.to_dict(orient="records")
#print(data)


db=client["insta_exercise"] #create a db called facebook_data
db.fb.insert_many(data)
print('data successfully added')





