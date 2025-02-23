from pydantic import BaseModel
from typing import List

class URLRequest(BaseModel):
    urls: List[str]

class QueryRequest(BaseModel):
    query: str
