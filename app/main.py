from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import get_answer

app = FastAPI(title="Insurance RAG Chatbot")


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG Chatbot Running"}


@app.post("/chat")
def chat(query: Query):
    return get_answer(query.question)