from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./blog.db'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = AsyncSession(engine, expire_on_commit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


