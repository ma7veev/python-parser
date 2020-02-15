# -*- coding: utf-8 -*-
import sys

import json
with open('env.json', 'r') as env:
    data=env.read()

# parse file
env_json = json.loads(data)
env_settings = env_json['settings']

try:    
    if sys.argv[1] == "catalog":
        from catalog import *
        parser = Catalog()
    elif sys.argv[1] == "one":
        parser = One()
    else: 
        print("put valid argument")
        sys.exit()
        
except IndexError:    
    print("put valid argument")
    sys.exit()


from connection import cursor
from connection import connection
from bs4 import BeautifulSoup
from urllib.request import urlopen
#cursor.execute("CREATE TABLE catalog(id serial PRIMARY KEY,name TEXT NOT NULL,url TEXT NOT NULL,status INTEGER NOT NULL DEFAULT 0);")
cursor.execute("SELECT * FROM catalog;")
record = cursor.fetchone()
print(record)
#sys.exit()
base_url = env_settings['base_url']
html_doc = urlopen(base_url + env_settings['catalog_url']).read()
soup = BeautifulSoup(html_doc, "html")

parser.parseItems(soup)
parser.writeItems(connection)
connection.commit()
#print(parser.items_data)

cursor.execute("SELECT version();")
record = cursor.fetchone()

#print(record)

"""
if(connection):
    cursor.close()
    connection.close()"""