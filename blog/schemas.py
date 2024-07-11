from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel

# if TYPE_CHECKING:
#     from __future__ import annotations  

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
        
class BlogCreator(ShowUser):
    name:str
    email:str
        
        


