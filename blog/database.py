from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./blog.db'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread" : False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    print('eeeeeeeeeee')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


