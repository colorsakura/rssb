from parser import parserxml
from jackett import Jackett

if __name__ == '__main__':
    keywords = "异世界舅舅"
    jackettIndexer = Jackett()
    indexers = jackettIndexer.get_indexers()
    for indexer in indexers:
        print(indexer['last_error'])
        if not indexer['last_error']:
            print(indexer['id'])
            xml = jackettIndexer.search(indexer['id'], keywords)
            print(type(xml))
            anime = parserxml(xml)
            print(anime)
