

class Item:

    items_data = []
    paginator = 0
    connection = None
    cursor = None
    item = ()
    settings = []

    def getUrl(self, url):
        self.cursor.execute("SELECT url, name FROM catalog WHERE id = %s", [self.paginator])
        item = self.cursor.fetchone()
        self.item = item

        return item[0] if item else None


    def parseItems(self, url):
        # TODO parse description or tags here

        href = self.item[0] + '/pdf'
        self.items_data.append((str(href), str(self.item[1])))


    def writeItems(self):
        import urllib.request
        g = urllib.request.urlopen(self.settings['base_url']+ self.items_data[0][0])
        name = 'files/'+self.item[1] + '.pdf'
        with open(name, 'b+w') as f:
            f.write(g.read())


    def updateStatus(self):
        sql = "UPDATE status SET last_catalog_url = %s"
        self.cursor.execute(sql, [self.paginator])
        sql = "UPDATE catalog SET status = 1 WHERE id = %s"
        self.cursor.execute(sql, [self.paginator])
        self.connection.commit()


    def setConnection(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def setSettings(self, settings):
        self.settings = settings
