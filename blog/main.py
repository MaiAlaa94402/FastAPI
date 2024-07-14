from fastapi import FastAPI
from . import models
from .database import engine
import blog
from .routers import blog, user


models.Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

