from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, userpdf, qa

app = FastAPI()
app.include_router(auth.router)
app.include_router(userpdf.router)
app.include_router(qa.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Clara Multi-User AI is running!"}