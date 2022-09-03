import requests


class Jackett():
    def __init__(self):
        '''获取 Jackett Cookie

        '''
        self.base_url = "http://jackett.52bilibili.com"
        password = "jackett"
        self.cookie = ""
        self.apikey = "ue9ko6yfbhpijxpcqmsmcu4k3a8oo0mj"
        payload = {'password': password}
        url = self.base_url + "/UI/Dashboard"
        s = requests.Session()
        s.post(url, data=payload)
        self.cookie = s.cookies

    def get_indexers(self):
        '''获取 Jackett Indexer

        :return:
        '''
        url = self.base_url + "/api/v2.0/indexers?configured=true"
        resp = requests.get(url, cookies=self.cookie)
        return resp.json()

    def search(self, indexer, keywords, categories=5000):
        url = self.base_url + "/api/v2.0/indexers/{}/results/torznab/".format(indexer)
        payload = {'apikey': self.apikey, 't': 'search', 'q': keywords, 'cat': categories}
        resp = requests.get(url, params=payload)
        return resp.content.decode('UTF-8')


if __name__ == '__main__':
    jackett = Jackett()
    print(jackett.search('acgrip', "异世界舅舅"))