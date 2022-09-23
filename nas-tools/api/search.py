from bangumi.bangumi import BangumiTV
from tmdb.tmdb import Tmdb


def search(keyword):
    """ 搜索关键词，(tv, movie)两个分类

    :param keyword: 关键词
    :return:
    """
    bangumi = BangumiTV()
    tmdb = Tmdb()
    result = {
        'total': 0,

    }
