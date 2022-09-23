from fastapi import FastAPI
from bangumi.bangumi import BangumiTV
from tmdb.tmdb import Tmdb

api = FastAPI()
bangumi = BangumiTV()
tmdb = Tmdb()


@api.get('/')
async def index():
    return {"code": 0, "data": "Hello World!"}


@api.get('/search/')
async def search(q: str, limit=8):
    return tmdb.search(q)


@api.get('/login')
async def login(user: str, password: str):
    return {}


@api.get('/logout')
async def logout():
    return {}


@api.post('/register')
async def register():
    pass


@api.get('/trend')
async def get_trend_list():
    return {}


@api.get('/all')
async def get_all(page=1, limit=10):
    return {}


@api.get('/detail/{tmdbid}')
def get_detail(tmdbid: int):
    return {}


@api.post('/subscribe/{tmdbid}')
async def subscribe(tmdbid: int, season: int):
    return {}


if __name__ == '__main__':
    import uvicorn
    import os

    if os.getenv('Debug'):
        pass
    uvicorn.run(app="api:api", debug=True, reload=True)
