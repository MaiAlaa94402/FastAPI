from fastapi import FastAPI
import blog
from .routers import blog, user, auth



app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

