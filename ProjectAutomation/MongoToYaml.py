from pymongo import MongoClient
from bson.json_util import dumps, loads
import json
import yaml
from yaml.loader import SafeLoader

client = MongoClient("localhost", 27017)

database = client["movie_db"]

movies = database.movies





cursor = movies.find({}, { "_id": 0 })
list_cur = list(cursor)
#json_data = dumps(list_cur)
#data = json.loads(json_data)

yaml_data = yaml.dump(list_cur[0], explicit_start = True, explicit_end = False, sort_keys=False, indent =3, default_style=None)



with open('data.txt', 'w') as file:
    file.write(yaml_data)

with open('data.txt', 'r') as f, open('dataout.yaml', 'w') as fo:
    for line in f:
        fo.write(line.replace("'",""))

#db = client.movie_db
#coll1 = db.movies
#for document in coll1.find():
    #print(document)
