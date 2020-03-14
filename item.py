

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


    def parseItems(self, soup):
        source_tag = soup.find("meta", {"name": "citation_journal_title"})
        source = source_tag.get("content") if source_tag else None

        href = self.item[0] + '/pdf'
        self.items_data.append([str(href), str(self.item[1]), str(source)])


    def writeItems(self):
        import urllib.request
        g = urllib.request.urlopen(self.settings['base_url']+ self.items_data[0][0])

        name = self.item[1]
        name = name[0:125]
        name = name.replace('/', '_')

        source = self.items_data[0][2] if self.items_data[0][2] else 'main'
        source = source[0:125]
        source = source.replace('/', '_')
        print(source)
        dir = self.settings['saving_folder']+source

        from pathlib import Path
        Path(dir).mkdir(parents=True, exist_ok=True)

        name = dir +'/'+name + '.pdf'
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


    def checkCaptcha(self, soup):
        captcha = soup.find("div", {"class": "g-recaptcha"})
        if captcha is None:
            return False
        else:
            return True

   # def parseTags(self, soup):
