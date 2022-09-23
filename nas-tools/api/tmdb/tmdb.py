import requests


class Tmdb:
    def __init__(self):
        self.baseurl = 'https://api.themoviedb.org/3'
        self.headers = {

        }
        self.apikey = 'b35d09cd066aaa90e9f51448fd78cd90'
        self.img_ur = 'https://image.tmdb.org/t/p/original'

    def init(self):
        pass

    def request(self, url, keyword=None):
        payload = {
            "api_key": self.apikey,
            "language": "zh-CN",
            "include_adult": "true",
        }
        if keyword:
            payload["query"] = keyword
        return requests.get(url, params=payload, headers=self.headers)

    def search_tv(self, keyword):
        url = self.baseurl + '/search/tv'
        resp = self.request(url, keyword=keyword).json()
        return self._img_url_handle(resp)

    def _img_url_handle(self, resp):
        items = resp['results']
        for item in items:
            if item['backdrop_path'] is not None:
                item['backdrop_path'] = self.img_ur + item['backdrop_path']
            if item['poster_path'] is not None:
                item['poster_path'] = self.img_ur + item['poster_path']
        return items

    def search_movie(self, keyword):
        url = self.baseurl + "/search/movie"
        resp = self.request(url, keyword=keyword).json()
        return self._img_url_handle(resp)

    def search(self, keyword):
        """通过关键词搜索相关tv, movie

        :param keyword:
        :return:
        """
        tv = self.search_tv(keyword)
        movie = self.search_movie(keyword)
        return tv + movie

    def search_by_tmdbid(self, tmdbid):
        pass

    def get_detail(self, tmdbid):
        pass

    def get_trand(self, media_type="tv", time_window="week"):
        url = self.baseurl + "/trending/{}/{}".format(media_type, time_window)
        return self.request(url=url).json()


if __name__ == '__main__':
    tmdb = Tmdb()

    # r = tmdb.search("总动员 ")
    t = tmdb.get_trand()
    print(t)
