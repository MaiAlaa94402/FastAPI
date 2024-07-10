from typing import Optional
from pydantic import BaseModel
      
        
class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        from_attributes = True
        
        
class Blog(BaseModel):
    title: str
    body: str
    creator: ShowUser


class ShowBlog(Blog):
    class Config():
        from_attributes = True