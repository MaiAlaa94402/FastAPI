from __future__ import annotations
from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    class Config():
        from_attributes = True
  
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: BlogCreator   
    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        from_attributes = True
    

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        from_attributes = True
        
class BlogCreator(BaseModel):
    name:str
    email:str
    
class Login(BaseModel):
    username:str
    password:str
    
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None        
        


