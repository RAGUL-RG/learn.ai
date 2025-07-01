
from fastapi import FastAPI
from routers import auth, userpdf, qa

app = FastAPI()

app.include_router(auth.router)
app.include_router(userpdf.router)
app.include_router(qa.router)
