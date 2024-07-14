from .. import models, schemas, hashing
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

Hash = hashing.Hash

def get_all(db:Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No users found')
    return users

def create(user: schemas.User, db:Session):
    hashed_password = Hash.bcrypt(user.password)
    new_user= models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id {id}')
    return user