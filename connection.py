# -*- coding: utf-8 -*-

import psycopg2


import json
with open('env.json', 'r') as env:
    data=env.read()

# parse file
env_json = json.loads(data)
env_connection = env_json['settings']['connection']

try:
    connection = psycopg2.connect(user = env_connection['user'],
                                  password = env_connection['password'],
                                  host = env_connection['host'],
                                  port = env_connection['port'],
                                  database = env_connection['database'])

    cursor = connection.cursor()


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

"""CREATE TABLE catalog(
   id serial PRIMARY KEY,
   name TEXT NOT NULL,
   url TEXT NOT NULL,
   status INTEGER NOT NULL DEFAULT 0
);"""

"""CREATE TABLE status(
   last_catalog_page INTEGER NOT NULL DEFAULT 0,
   last_catalog_url TEXT
);
INSERT INTO status (last_catalog_page, last_catalog_url) VALUES (0, '');
"""
