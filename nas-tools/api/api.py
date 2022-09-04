from fastapi import FastAPI

api = FastAPI()


@api.get('/')
def index():
    return {"code": 0, "data": "Hello World!"}


@api.get('/search')
def search():
    return {}
