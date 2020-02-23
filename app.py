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
        url = env_settings['catalog_url']
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

base_url = env_settings['base_url']

cursor.execute("SELECT last_catalog_page FROM status;")
status = cursor.fetchone()
last_page = status[0]

i = last_page - 1

while i > 0:
    parser.paginator = i
    next_url = parser.getUrl(url)

    html_doc = urlopen(base_url + next_url).read()
    soup = BeautifulSoup(html_doc, "html")

    parser.parseItems(soup)

    parser.writeItems(connection)
    parser.items_data =[]
    parser.updateStatus(connection, i)

    i -= 1


cursor.execute("SELECT version();")
record = cursor.fetchone()




"""
if(connection):
    cursor.close()
    connection.close()"""