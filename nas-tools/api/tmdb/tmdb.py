import requests


class Tmdb():
    def __init__(self):
        self.baseurl = 'https://api.themoviedb.org/3'
        self.header = {

        }
        self.apikey = 'b35d09cd066aaa90e9f51448fd78cd90'
        self.imgurl = 'https://image.tmdb.org/t/p/original'

    def init(self):
        pass

    def request(self, url, keyword):
        payload = {
            "api_key": self.apikey,
            "language": "zh-CN",
            "query": keyword,
            "include_adult": "true",
        }
        return requests.get(url, params=payload, headers=self.header)

    def tv(self, keyword):
        url = self.baseurl + '/search/tv'
        resp = self.request(url, keyword).json()
        items = resp['results']
        for item in items:
            if item['backdrop_path'] != None:
                item['backdrop_path'] = self.imgurl + item['backdrop_path']
            if item['poster_path'] != None:
                item['poster_path'] = self.imgurl + item['poster_path']
        return items

    def movie(self, keyword):
        url = self.baseurl + "/search/movie"
        resp = self.request(url, keyword).json()
        items = resp['results']
        for item in items:
            if item['backdrop_path'] != None:
                item['backdrop_path'] = self.imgurl + item['backdrop_path']
            if item['poster_path'] != None:
                item['poster_path'] = self.imgurl + item['poster_path']
        return items

    def search(self, keyword):
        tv = self.tv(keyword)
        movie = self.movie(keyword)
        return tv + movie

    def search_by_tmdbid(self, tmdbid):
        pass


if __name__ == '__main__':
    tmdb = Tmdb()

    r = tmdb.search("总动员 ")
    print(r)
    # for result in resp:
    #     print(result)
    #
    # season = Season()
    # show_season = season.details(82684, 1)
    # print(show_season)
