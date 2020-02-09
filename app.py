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


base_url = env_settings['base_url']
html_doc = urlopen(base_url + env_settings['catalog_url']).read()
soup = BeautifulSoup(html_doc)

parser.parseItems(soup)
print(parser.items_data)

cursor.execute("SELECT version();")
record = cursor.fetchone()

print(record)

"""
if(connection):
    cursor.close()
    connection.close()"""