from fastapi import APIRouter, status, Depends
from blog import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(User: schemas.User, db:Session=Depends(get_db)):
    return user.create(User, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    return user.get(id, db)

@router.get('/', response_model=list[schemas.ShowUser])
def all(db:Session=Depends(get_db)):
    return user.get_all(db)