# -*- coding: utf-8 -*-

base_url = ''
html_doc = urlopen(base_url + '').read()
soup = BeautifulSoup(html_doc)
list_items = soup.find("div", {"class": "full"}).find("ul", {"class": "list"}).find_all("li")
#print(list_items)
#print(soup)
for item in list_items:
    link = item.find("a")
    href = link.get("href")
    title = link.find("div", {"class": "title"}).contents[0]
    print( "\n")
    print(href)
    print( "\n")
    print(title)
    print( "\n")
    
    
    
    
if(connection):
    cursor.close()
    connection.close()


def openItem(link):
    item_doc = urlopen(base_url + link).read()
    item_soup = BeautifulSoup(html_doc)