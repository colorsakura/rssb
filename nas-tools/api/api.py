from fastapi import FastAPI
from bangumi.bangumi import BangumiTV

api = FastAPI()
bangumi = BangumiTV()


@api.get('/')
async def index():
    return {"code": 0, "data": "Hello World!"}


@api.get('/search/{keywords}')
async def search(keywords: str):
    return bangumi.search(keywords)


@api.get('/login')
async def login():
    return {}


@api.post('/register')
async def register():
    pass


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="api:api", debug=True, reload=True)
