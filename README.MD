SIMPLE PARSER for pdf articles

**REQUIREMENTS**

SQL-type database
PYTHON 3.6


**DB structure**
"""CREATE TABLE catalog(
   id serial PRIMARY KEY,
   name TEXT NOT NULL,
   url TEXT NOT NULL,
   status INTEGER NOT NULL DEFAULT 0
);"""

"""CREATE TABLE status(
   last_catalog_page INTEGER NOT NULL DEFAULT 9999,
   last_catalog_url INTEGER
);
INSERT INTO status (last_catalog_page, last_catalog_url) VALUES (9999, NULL);
"""

**SETTINGS FILE**

env.json file in root

`{
    "settings":{
        "connection":{
            "user":"parser",
            "password":"parser",
            "host":"127.0.0.1",
            "port":"5432",
            "database":"parser"
        },
        "base_url":"https://cyberleninka.ru",
        "catalog_url":"/article/c/...",
        "item_url":"/article/c/...",
        "last_page":9999,
        "saving_folder":"/home/.../articles/"
    }
}`

**HOW IT WORKS**
It starts from last page of items catalog. Last page number should be set up in database status.last_catalog_page of in settings file in settings.last_page
"Catalog" method parses list of items links, and "one" method saves pdf file in folder from settings.saving_folder


`python3.6 app.py catalog`
`python3.6 app.py one`
