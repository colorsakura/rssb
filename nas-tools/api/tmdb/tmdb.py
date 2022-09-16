from tmdbv3api import TMDb, TV, Season

if __name__ == '__main__':
    tmdb = TMDb()
    tmdb.api_key = 'b35d09cd066aaa90e9f51448fd78cd90'
    tmdb.language = 'zh-CN'
    tmdb.debug = True

    tv = TV()

    resp = tv.search("关于我转生变成史莱姆这档事 ")
    for result in resp:
        print(result)

    season = Season()
    show_season = season.details(82684,1)
    print(show_season)