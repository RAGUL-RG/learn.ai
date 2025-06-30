from fastapi import APIRouter, UploadFile, File, Depends
from auth import get_current_user
from utils import save_user_pdf, learn_user_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...), user=Depends(get_current_user)):
    path = save_user_pdf(user, file)
    learn_user_pdf(user, path)
    return {"msg": "Learned PDF successfully"}