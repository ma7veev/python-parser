# -*- coding: utf-8 -*-


class Catalog:

    items_data = []
    paginator = 0

    def getUrl(self, url):

        if self.paginator != 0:
            url = url + '/' + str(self.paginator)


        return url

    def parseItems(self, soup):

        list_items = soup.find("div", {"class": "full"}).find("ul", {"class": "list"}).find_all("li")

        for item in list_items:
            link = item.find("a")
            href = link.get("href")
            title = link.find("div", {"class": "title"}).contents[0]
            list = (str(title), str(href))
            self.items_data.append(list)


    def writeItems(self, connection):
        cursor = connection.cursor()
        sql = "INSERT INTO catalog(name,url) VALUES (%s, %s)"
        cursor.executemany(sql,self.items_data)
        connection.commit()


    def updateStatus(self, connection, last_page):
        cursor = connection.cursor()
        sql = "UPDATE status SET last_catalog_page = %s"
        cursor.execute(sql, [last_page])
        connection.commit()