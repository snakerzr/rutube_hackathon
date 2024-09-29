from pydantic import BaseModel


class Request(BaseModel):
    question: str


class Response(BaseModel):
    answer: str
    class_1: str
    class_2: str

class ResponseClassify(BaseModel):
    answer_1: float
    class_1: str
    answer_2: float
    class_2: str