from blog import schemas
from blog.database import get_db
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..repository import blog
from .. import oauth2




router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/',response_model=list[schemas.ShowBlog])
async def all(db:AsyncSession=Depends(get_db), get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return await blog.get_all(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def get_blog(id, response:Response, db:AsyncSession=Depends(get_db)):
    return await blog.get(id, db)


@router.post('/{user_id}', status_code=status.HTTP_201_CREATED)
async def create_blog(user_id: int, requests: schemas.Blog, db:AsyncSession=Depends(get_db)):
    return await blog.create(user_id, requests, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, request :schemas.Blog, db:AsyncSession=Depends(get_db)):
    return await blog.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id, db: AsyncSession=Depends(get_db)):
    return await blog.destroy(id, db)