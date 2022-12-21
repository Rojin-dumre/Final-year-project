from pymongo import MongoClient
from bson.json_util import dumps, loads
import json
import yaml
# from yaml.loader import SafeLoader
import os
import subprocess
import re



client = MongoClient("localhost", 27017)

database = client["jsontoyaml"]

movies = database.details





cursor = movies.find({}, { "_id": 0 })
list_cur = list(cursor)
#json_data = dumps(list_cur)
#data = json.loads(json_data)
#print(list_cur)
yaml_data = yaml.dump(list_cur, explicit_start = False, explicit_end = False, sort_keys=False, indent =3, default_style=None)

#print(yaml_data)
 
with open('data.txt', 'w') as file:
    file.write(yaml_data)

with open('data.txt', 'r') as f, open('dataout.txt', 'w') as fo:
    for line in f:
        fo.write(line.replace("'",""))
        #fo.write(line.replace("- ","\n- "))

with open('dataout.txt', 'r') as g, open('databuff.txt', 'w') as go:
    for line in g:
        go.write(line.replace("-  Router:", ""))

with open('databuff.txt', 'r') as h, open('datafinal.txt', 'w') as ho:
    for line in h:
        global line1
        global line3
        line3 = None
        line1 = None
        if re.search('R.+', line):
            line3 = line
            #print(line3)
            line2 = str(line.strip()) + ":"
            line1 = line2.replace("- ", "")
            #print(line)
            #print(line1)
        ho.write(line.replace(str(line3), str(line1)+"\n\n"))

directory = '/home/rojin/Documents/jsontoyamlv4/jsontoyaml/python'
filename = "hosts.yaml"
file_path = os.path.join(directory, filename)

with open('datafinal.txt', 'r') as i, open('datafinal1.txt', 'w') as io:
    for line in i:
        io.write(line.replace("   - ", "\n      - "))


with open('datafinal1.txt', 'r') as j, open(file_path, 'w') as jo:
    for line in j:
        jo.write(line.replace("   __v: 0", ''))

#filename = 'hosts.txt'
#line = subprocess.check_output(['head', '-n', '-1', filename])
#line = line.decode('utf-8')

#with open('hosts.yaml', 'w') as file:
    #file.write(line)


if os.path.exists("data.txt"):
   os.remove("data.txt")
else:
    print("no file")

if os.path.exists("databuff.txt"):
    os.remove("databuff.txt")
else:
   print("no file")

if os.path.exists("datafinal.txt"):
   os.remove("datafinal.txt")
else:
   print("no file")

if os.path.exists("dataout.txt"):
   os.remove("dataout.txt")
else:
   print("no file")

if os.path.exists("datafinal1.txt"):
   os.remove("datafinal1.txt")
else:
    print("no file")
#db = client.movie_db
#coll1 = db.movies
#for document in coll1.find():
    #print(document)
    
