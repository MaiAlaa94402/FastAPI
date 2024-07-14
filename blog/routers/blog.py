from sqlalchemy.orm import Session
from blog import schemas
from blog.database import get_db
from fastapi import APIRouter, Depends, Response, status
from ..repository import blog
from .. import oauth2

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/',response_model=list[schemas.ShowBlog])
def all(db:Session=Depends(get_db), get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog(id, response:Response, db:Session=Depends(get_db)):
    return blog.get(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.ShowBlog, db:Session=Depends(get_db)):
    return blog.create(blog, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, blog :schemas.Blog, db:Session=Depends(get_db)):
    return blog.update(id, blog, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session=Depends(get_db)):
    return blog.destroy(id, db)