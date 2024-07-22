from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, JWTtoken
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from sqlalchemy.ext.asyncio import AsyncSession




router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm=Depends(), db: AsyncSession=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')

    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}
 