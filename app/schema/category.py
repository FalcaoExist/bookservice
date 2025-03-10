from pydantic import BaseModel
from typing import Any, Dict

class Teste(BaseModel):
    send: bool

class CreateCategoryResponse(BaseModel):
    status: Any
    path: str
    mensage: str | None = None

class RequestCreateCategory(BaseModel):
    name: str
    idade: int

