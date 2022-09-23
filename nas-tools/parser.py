import xml.sax


class Parser(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self.tag = ""
        self.depth = []  # 记录树
        self.result = []
        self.title = ""
        self.guid = ""
        self.type = ""
        self.site = ""
        self.page = ""
        self.date = ""
        self.size = ""
        self.grabs = ""
        self.link = ""
        self.category = []
        self.seeders = ""
        self.peers = ""
        self.downloadvolumefactor = ""
        self.uploadvolumefactor = ""

    def startElement(self, name, attrs):
        self._charBuffer = []
        self.tag = name
        self.depth.append(name)
        if self.tag == "item":
            self.clearField()

    def _flushCharBuffer(self):
        s = ''.join(self._charBuffer)
        return s

    def characters(self, content):
        self._charBuffer.append(content)
        if self.depth[len(self.depth) - 2] == "item":
            if self.tag == "title":
                self.title = self._charBuffer
            elif self.tag == "guid":
                self.guid = self._charBuffer
            elif self.tag == "jackettindexer":
                self.site = self._charBuffer
            elif self.tag == "type":
                self.type = self._charBuffer
            elif self.tag == "comments":
                self.page = self._charBuffer
            elif self.tag == "pubDate":
                self.date = self._charBuffer
            elif self.tag == "size":
                self.size = self._charBuffer
            elif self.tag == "grabs":
                self.grabs = self._charBuffer
            elif self.tag == "link":
                self.link = self._charBuffer
            elif self.tag == "category":
                self.category.append(''.join(self._charBuffer))
            else:
                pass
        else:
            pass

    def endElement(self, name):
        self.tag = name
        if self.tag == "item":
            item = {
                "title": clean_string(''.join(self.title)),
                "guid": clean_string(''.join(self.guid)),
                "type": clean_string(''.join(self.type)),
                "site": clean_string(''.join(self.site)),
                "page": clean_string(''.join(self.page)),
                "date": clean_string(''.join(self.date)),
                "size": clean_string(''.join(self.size)),
                "grab": clean_string(''.join(self.grabs)),
                "link": clean_string(''.join(self.link)),
                "category": self.category,
                "seeders": clean_string(''.join(self.seeders)),
                "peers": clean_string(self.peers),
                "downloadvolumefactor": clean_string(''.join(self.downloadvolumefactor)),
                "uploadvolumefactor": clean_string(''.join(self.uploadvolumefactor))
            }
            self.result.append(item)
            self.clearField()
        if self.tag == self.depth[-1]:
            self.depth.pop()

    def clearField(self):
        self.title = ""
        self.guid = ""
        self.type = ""
        self.site = ""
        self.page = ""
        self.date = ""
        self.size = ""
        self.grabs = ""
        self.link = ""
        self.category = []
        self.seeders = ""
        self.peers = ""
        self.downloadvolumefactor = ""
        self.uploadvolumefactor = ""


def parserxml(xmlstring):
    handler = Parser()
    parser = xml.sax.parseString(xmlstring, handler)
    # 重写 ContextHandler
    return handler.result


def clean_string(string):
    string.strip()
    string.replace('\n', '')
    temp = ' '.join(string.split())
    return temp


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = Parser()
    parser.setContentHandler(Handler)

    parser.parse("test.xml")
    print(Handler.result)
