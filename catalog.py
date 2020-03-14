# -*- coding: utf-8 -*-


class Catalog:

    items_data = []
    paginator = 0
    connection = None
    cursor = None
    settings = []

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


    def writeItems(self):
        sql = "INSERT INTO catalog(name,url) VALUES (%s, %s)"
        self.cursor.executemany(sql,self.items_data)
        self.connection.commit()


    def updateStatus(self):
        sql = "UPDATE status SET last_catalog_page = %s"
        self.cursor.execute(sql, [self.paginator])
        self.connection.commit()

    def setConnection(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def setSettings(self, settings):
        self.settings = settings

    def checkCaptcha(self, soup):
        captcha = soup.find("div", {"class": "g-recaptcha"})
        if captcha is None:
            return False
        else:
            return True
