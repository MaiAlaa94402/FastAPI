from fastapi import FastAPI
from . import models
from .database import engine
import blog
from .routers import blog, user, auth
import asyncio


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

# asyncio.run(init_models())



    # await engine.dispose()

# asyncio.run(init_models())

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

