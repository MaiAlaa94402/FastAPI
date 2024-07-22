from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
import aiohttp
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

def get_all(db: AsyncSession):
    blogs = db.query(models.Blog).all()
    return blogs

# async def create(id:int, blog: schemas.Blog, db:Session):
#     async with aiohttp.ClientSession() as session:
#         new_blog = models.Blog(title=blog.title, body=blog.body, user_id=id)
#         db.add(new_blog)
#         await db.commit()
#         db.refresh(new_blog)
#     return new_blog

async def create(id:int, blog: schemas.Blog, db:AsyncSession):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=id)
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog

async def destroy(id:int, db:AsyncSession):
    blog = await db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    await db.commit()
    db.close()
    if blog>0:
        return f'Blog is deleted'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')

async def get(id:int, db:AsyncSession):
    blog = await db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f'Blog with id {id} is not available')
    return blog

async def update(id:int, blog:schemas.Blog, db:AsyncSession):
    updated_blog = await db.query(models.Blog).filter(models.Blog.id == id)
    if not updated_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    updated_blog.update({'title':blog.title, 'body': blog.body})
    db.commit()
    db.close()
    return f'Blog is updated'