from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./blog.db'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread" : False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = AsyncSession(engine, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


