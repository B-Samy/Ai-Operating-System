
from fastapi import FastAPI
from schema import ChatRequest, Chatresponse
from importnb import Notebook

with Notebook():
    from notebook import ask_question

app = FastAPI(title="AIOS API")


@app.post("/chat", response_model=Chatresponse)
def chat(request: ChatRequest):
    reply = ask_question(request.message)
    return Chatresponse(reply=reply)
