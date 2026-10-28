from pydantic import BaseModel , Field 
from typing import Annotated , AnyStr


class ChatRequest(BaseModel):
    message : str = Field(min_length=1 , max_length=5000)

class Chatresponse(BaseModel):
    reply : str 