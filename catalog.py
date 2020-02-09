# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Catalog:
    
    items_data = {}
    
        
    def parseItems(self, soup):
        
        list_items = soup.find("div", {"class": "full"}).find("ul", {"class": "list"}).find_all("li")
        
        for item in list_items:
            link = item.find("a")
            href = link.get("href")
            title = link.find("div", {"class": "title"}).contents[0]
            self.items_data[title]=href
        
        
        
        
    
    
    def writeItems(cursor):
        sql = """INSERT INTO catalog(name,url)
                 VALUES(%n,%u) RETURNING vendor_id;"""
        for name,url in self.items_data:
            cursor.execute(sql, (name,url))