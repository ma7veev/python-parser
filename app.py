# -*- coding: utf-8 -*-
import sys

import json
with open('env.json', 'r') as env:
    data=env.read()

# parse file
env_json = json.loads(data)
env_settings = env_json['settings']


from connection import cursor
from bs4 import BeautifulSoup
from urllib.request import urlopen


cursor.execute("SELECT version();")
record = cursor.fetchone()

print(record)
print(sys.argv[1])