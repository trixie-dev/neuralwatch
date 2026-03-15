from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class AIModelCreate(BaseModel):
    name: str
    version: str
    endpoint_url: str


class AIModelOut(BaseModel):
    id: int
    name: str
    version: str
    status: str
    endpoint_url: str
    latency: float
    cpu_load: float
    owner: str

    class Config:
        from_attributes = True
        

class Token(BaseModel):
    access_token: str
    token_type: str