import xml.sax
from array import array


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
        self.category = ""
        self.seeders = ""
        self.peers = ""
        self.downloadvolumefactor = ""
        self.uploadvolumefactor = ""

    def startElement(self, name, attrs):
        # print("这是startElement: ", name)
        self._charBuffer = []
        self.tag = name
        self.depth.append(name)
        if self.tag == "item":
            # print("开始解析xml内容")
            self.clearField()

    def _flushCharBuffer(self):
        s = ''.join(self._charBuffer)
        # print(self._charBuffer)
        return s

    def characters(self, content):
        self._charBuffer.append(content)
        # print(self._charBuffer)
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
                self.category = self._charBuffer
            else:
                print("未处理元素")
        else:
            pass

    def endElement(self, name):
        self.tag = name
        # print("这是endElement: ", name)
        if self.tag == "item":
            item = {
                "title": ''.join(self.title).strip(),
                "guid": ''.join(self.guid).strip(),
                "type": ''.join(self.type).strip(),
                "site": ''.join(self.site).strip(),
                "page": ''.join(self.page).strip(),
                "date": ''.join(self.date).strip(),
                "size": ''.join(self.size).strip(),
                "grab": ''.join(self.grabs).strip(),
                "link": ''.join(self.link).strip(),
                "category": ''.join(self.category).strip(),
                "seeders": ''.join(self.seeders).strip(),
                "peers": self.peers.strip(),
                "downloadvolumefactor": self.downloadvolumefactor.strip(),
                "uploadvolumefactor": ''.join(self.uploadvolumefactor).strip()
            }
            self.result.append(item)
            self.clearField()
        # print(self.result)
        if self.tag == self.depth[len(self.depth) - 1]:
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
        self.category = ""
        self.seeders = ""
        self.peers = ""
        self.downloadvolumefactor = ""
        self.uploadvolumefactor = ""

    def endDocument(self):
        print(self.result)
        return self.result


def parserxml(xmlstring):
    parser = xml.sax.parseString(xmlstring, handler=Parser())
    # 重写 ContextHandler
    Handler = Parser()

    return parser


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = Parser()
    parser.setContentHandler(Handler)

    parser.parse("test.xml")
