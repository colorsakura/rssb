import requests

class Jackett():
    def __init__(self):
        '''

        '''
        self.base_url = "http://jackett.52bilibili.com"
        password = "jackett"
        self.cookie = ""
        payload = {'password': password}
        url = self.base_url + "/UI/Dashboard"
        s = requests.Session()
        s.post(url, data=payload)
        self.cookie = s.cookies

    def get_indexers(self):
        url = self.base_url + "/api/v2.0/indexers?configured=true"
        resp = requests.get(url, cookies=self.cookie)
        return resp.json()