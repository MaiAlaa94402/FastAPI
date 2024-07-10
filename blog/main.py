from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .hashing import Hash
import blog
from .routers import blog


models.Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(blog.router)


@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create_blog(blog: schemas.ShowBlog, db:Session=Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# @app.get('/blog/',response_model=list[schemas.ShowBlog], tags=["blogs"])
# def all(db:Session=Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete(id, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    db.close()
    if blog>0:
        return f'Blog is deleted'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(id, blog :schemas.Blog, db:Session=Depends(get_db)):
    updated_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not updated_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    updated_blog.update({'title':blog.title, 'body': blog.body})
    db.commit()
    db.close()
    return f'Blog is updated'



@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
def get_blog(id, response:Response, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f'Blog with id {id} is not available')
    return blog



@app.post('/user', status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(user: schemas.User, db:Session=Depends(get_db)):
    hashed_password = Hash.bcrypt(user.password)
    new_user= models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/get/{id}', response_model=schemas.ShowUser, tags=["users"])
def get_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id {id}')
    return user

@app.get('/get/', response_model=list[schemas.ShowUser], tags=["users"])
def all(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No users found')
    return users