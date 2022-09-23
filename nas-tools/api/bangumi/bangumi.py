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
        {'results': 1, 'list': [{'id': 339326, 'url': 'http://bgm.tv/subject/339326', 'type': 2, 'name': '異世界おじさん', 'name_cn': '异世界舅舅', 'summary': '', 'air_date': '', 'air_weekday': 0, 'images': {'large': 'http://lain.bgm.tv/pic/cover/l/1a/75/339326_v466V.jpg', 'common': 'http://lain.bgm.tv/pic/cover/c/1a/75/339326_v466V.jpg', 'medium': 'http://lain.bgm.tv/pic/cover/m/1a/75/339326_v466V.jpg', 'small': 'http://lain.bgm.tv/pic/cover/s/1a/75/339326_v466V.jpg', 'grid': 'http://lain.bgm.tv/pic/cover/g/1a/75/339326_v466V.jpg'}}]}

        '''
        url = self.baseurl + "/search/subject/{}".format(keywords)
        params = {
            "type": 2,
            "responseGroup": "small",
        }
        resp = requests.get(url, params=params, headers=self.headers)
        return resp.json()

    def search_by_id(self, bgid):
        '''获取详细信息

        :param bgid:
        :return:
        '''
        url = self.baseurl + "/v0/subjects/{}".format(bgid)
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    def get_names(self, bgid):
        detail = self.search_by_id(bgid)
        names = []
        names.append(detail['name'])
        names.append(detail['name_cn'])
        for info in detail['infobox']:
            if info['key']  in ['中文名', '别名']:
                print(info['value'])
                if isinstance(info['value'], str):
                    names.append(info['value'])
                elif isinstance(info['value'], list):
                    for item in info['value']:
                        names.append(item['v'])
                else:
                    print("BangumiTV 别名解析出错...")
        return set(names)


if __name__ == '__main__':
    bangumi = BangumiTV()
    # print(bangumi.search("异世界归来的舅舅"))
    # print(bangumi.search_by_id(339326))
    print(bangumi.get_names(339326))
