from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import get_db
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/blog/',response_model=list[schemas.ShowBlog], tags=["blogs"])
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs