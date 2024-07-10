from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# @app.get('/blog')
# def index(limit: int=10, published: bool=True, sort: Optional[str] = None):
#     if(published):
#         return{'data': f'{limit} published blogs from the db'}
#     else:
#         return {'data': f'{limit} blogs from the db'}


# @app.get('/blogs/unpublished')
# def unpublished():
#     return {'data' : 'all unpublished blogs'}


# @app.get('/blogs/{id}')
# def show(id: int):
#     return {'data' : id}



# @app.get('/blogs/{id}/comments')
# def comments(id):
#     return {'data' : {'1', '2'}}


# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]

# @app.post('/blog')
# def create_blog(blog: Blog):
#     return {'data': f'{blog} is created'}