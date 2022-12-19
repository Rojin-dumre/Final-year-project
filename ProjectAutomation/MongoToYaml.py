from pymongo import MongoClient
from bson.json_util import dumps, loads
import json
import yaml
from yaml.loader import SafeLoader
import os

client = MongoClient("localhost", 27017)

database = client["movie_db"]

movies = database.movies





cursor = movies.find({}, { "_id": 0 })
list_cur = list(cursor)
#json_data = dumps(list_cur)
#data = json.loads(json_data)

yaml_data = yaml.dump(list_cur[0], explicit_start = False, explicit_end = False, sort_keys=False, indent =3, default_style=None)


 
with open('data.txt', 'w') as file:
    file.write(yaml_data)

with open('data.txt', 'r') as f, open('dataout.txt', 'w') as fo:
    for line in f:
        fo.write(line.replace("'",""))
        #fo.write(line.replace("- ","\n- "))

with open('dataout.txt', 'r') as g, open('hosts.yaml', 'w') as go:
    for line in g:
        go.write(line.replace("-", '\n\n      -'))

if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("no file")

if os.path.exists("dataout.txt"):
    os.remove("dataout.txt")
else:
    print("no file")

