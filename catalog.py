# -*- coding: utf-8 -*-


class Catalog:

    items_data = []


    def parseItems(self, soup):

        list_items = soup.find("div", {"class": "full"}).find("ul", {"class": "list"}).find_all("li")

        for item in list_items:
            link = item.find("a")
            href = link.get("href")
            title = link.find("div", {"class": "title"}).contents[0]
            self.items_data.append((title, href, 1))






    def writeItems(self, connection):

        values = ', '.join(map(str, self.items_data))

        sql = "INSERT INTO catalog(name,url,status) VALUES{}".format(values)
        connection.cursor().execute(sql)
        connection.commit()