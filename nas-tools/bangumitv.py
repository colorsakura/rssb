import requests

class BangumiTV():
    def __init__(self):
        self.baseurl = "https://api.bgm.tv"
        self.headers = {
            "accept": "application/json",
            "user-agent": "ACG-SAKURA/nas-tools"
        }

    def search(self, keywords, **kwargs):
        '''通过关键字搜索内容

        :param keywords:
        :param kwargs:
        :return: json()
        '''
        url = self.baseurl + "/search/subject/{}".format(keywords)
        params = {
            "type": 2,
            "responseGroup": "small",
        }
        resp = requests.get(url, params=params, headers=self.headers)
        return resp.json()

    def search_by_id(self, id):
        url = self.baseurl + "/v0/subjects/{}".format(id)
        headers = {
            "accept": "application/json"
        }
        resp = requests.get(url, headers=self.headers)
        return resp.json()




if __name__ == '__main__':
    bangumi = BangumiTV()
    print(bangumi.search("异世界"))
    print(bangumi.search_by_id(282741))