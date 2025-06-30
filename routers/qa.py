from fastapi import APIRouter, Depends
from pydantic import BaseModel
from auth import get_current_user
from utils import answer_user_question

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    lang_in: str = "en"
    lang_out: str = "en"
    mode: str = "text"

@router.post("/ask")
def ask_question(req: QuestionRequest, user=Depends(get_current_user)):
    return answer_user_question(user, req.question, req.lang_in, req.lang_out, req.mode)