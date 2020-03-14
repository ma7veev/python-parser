# -*- coding: utf-8 -*-
import sys

import json
with open('env.json', 'r') as env:
    data=env.read()

# parse file
env_json = json.loads(data)
env_settings = env_json['settings']

from connection import cursor
from connection import connection
cursor.execute("SELECT * FROM status;")
status = cursor.fetchone()

try:    
    if sys.argv[1] == "catalog":
        from catalog import *
        parser = Catalog()
        url = env_settings['catalog_url']

        last_page = status[0] if status else 9999

    elif sys.argv[1] == "one":
        from item import *
        parser = Item()
        url = env_settings['item_url']
        last_page = status[1] if status else None
        if last_page  is  None:
            cursor.execute("SELECT max(id) FROM catalog WHERE status = 0;")
            id = cursor.fetchone()
            last_page  = id[0] if id else 9999
    else: 
        print("put valid argument")
        sys.exit()
        
except IndexError:    
    print("put valid argument")
    sys.exit()


from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = env_settings['base_url']

parser.setConnection(connection)
parser.setSettings(env_settings)
i = last_page - 1

while i > 0:
    parser.paginator = i
    next_url = parser.getUrl(url)
    print(next_url)
    html_doc = urlopen(base_url + next_url).read()

    soup = BeautifulSoup(html_doc, "html.parser")
    if parser.checkCaptcha(soup):
        print("CAPTCHA ERROR!")
        sys.exit()
    parser.parseItems(soup)

    parser.writeItems()
    parser.items_data =[]
    parser.updateStatus()

    i -= 1






"""
if(connection):
    cursor.close()
    connection.close()"""