import json

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
		# TODO: 应该设计成通用的遍历函数，目前缺乏维护性
		items = resp['results']
		for item in items:
			if item['backdrop_path'] is not None:
				item['backdrop_path'] = self.img_ur + item['backdrop_path']
			if item['poster_path'] is not None:
				item['poster_path'] = self.img_ur + item['poster_path']
		return json.dumps(items, ensure_ascii=False)

	def search_movie(self, keyword):
		url = self.baseurl + "/search/movie"
		resp = self.request(url, keyword=keyword).json()
		return self._img_url_handle(resp)

	def search(self, keyword):
		r"""通过关键词搜索相关tv, movie

		:param keyword:
		:return:
		"""
		tv = self.search_tv(keyword)
		movie = self.search_movie(keyword)
		return tv + movie

	def get_season(self, tmdbid):
		r"""获取TV的季数

		:param tmdbid:
		:return:
		"""
		url = self.baseurl + "/tv/{}".format(str(tmdbid))
		return json.dumps(self.request(url).json()['seasons'], ensure_ascii=False)

	def get_detail(self, tmdbid, season=-1):
		"""目前只有TV有season，获取集数

		:param tmdbid:
		:param season:
		:return:
		"""
		if season == -1:
			return {}
		url = self.baseurl + "/tv/{}/season/{}".format(str(tmdbid), season)
		resp = self.request(url).json()
		return json.dumps(resp, ensure_ascii=False)

	def get_trand(self, media_type="tv", time_window="week"):
		url = self.baseurl + "/trending/{}/{}".format(media_type, time_window)
		return self.request(url=url).json()


if __name__ == '__main__':
	tmdb = Tmdb()

	r = tmdb.search("overlord ")
	t = tmdb.get_season(64196)
	print(t)
