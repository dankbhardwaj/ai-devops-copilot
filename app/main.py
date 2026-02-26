from fastapi import FastAPI
from app.models.request_models import AskRequest
from app.services.ask_service import process_question

app = FastAPI()

@app.post("/ask")
def ask_question(request: AskRequest):
    answer = process_question(request.question)
    return {"message": answer}