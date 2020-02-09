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
       
