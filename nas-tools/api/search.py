from bangumi.bangumi import BangumiTV
from tmdb.tmdb import Tmdb


def search_by_keyword(keyword):
    """通过关键词从TMDB搜索电影、TV条目

    :param keyword: 搜索关键词;
    :return: {‘total’: num, 'result': [{'name': '异世界舅舅', 'origin_name': '異世界おじさん', 'origin_country': 'JP', 'id': 127714, ‘first_air_date’: '2022-07-06', 'overview': '简单描述', 'poster': '', 'backdrop': ''}]}
    """
    """ 搜索关键词，(tv, movie)两个分类

    :param keyword: 关键词
    :return:
    """
    bangumi = BangumiTV()
    tmdb = Tmdb()
    result = {
        'total': 0,

    }
