from fastapi import APIRouter, status, Depends
from blog import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user
from sqlalchemy.ext.asyncio import AsyncSession



router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(User: schemas.User, db:AsyncSession=Depends(get_db)):
    return await user.create(User, db)

@router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id:int, db:AsyncSession=Depends(get_db)):
    return await user.get(id, db)

@router.get('/', response_model=list[schemas.ShowUser])
async def all(db:AsyncSession=Depends(get_db)):
    return await user.get_all(db)