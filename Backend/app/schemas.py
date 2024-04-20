from pydantic import BaseModel

class Token(BaseModel):
    token: str

class Diary(Token):
    email: str

class RetrieveDiary(BaseModel):
    email: str