from .. import models, schemas, hashing
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


Hash = hashing.Hash

async def get_all(db:AsyncSession):
    query = select(models.User)
    result = await db.execute(query)
    users = result.scalars().all()
    # users = await db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No users found')
    return users

async def create(user: schemas.User, db:AsyncSession):
    hashed_password = Hash.bcrypt(user.password)
    new_user= models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get(id:int, db:AsyncSession):
    user = await db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id {id}')
    return user