import re

import uvicorn
from fastapi import FastAPI

from src.classifier import id2label_one, id2label_two, onnx_clf_one, onnx_clf_two
from src.rag.main import rag_pipeline
from src.rag.retriever import create_chroma_db, get_collection

from .schema import Request, Response, ResponseClassify

create_chroma_db()

collection = get_collection()

app = FastAPI()

@app.get("/")
def index():
    return {"text": "Интеллектуальный помощник оператора службы поддержки."}


@app.post("/predict")
async def get_reponse(request: Request) -> Response:
    answer = rag_pipeline(request.question)['actual_response']
    if re.findall('не знаю|не могу|нет ответа', answer.lower()):
        class_1 = 'None'
        class_2 = 'None'
    else:
        result_one = onnx_clf_one(request.question)
        class_1 = id2label_one[result_one[0]['label'].split('_')[1]]
        result_two = onnx_clf_two(request.question)
        class_2 = id2label_two[result_two[0]['label'].split('_')[1]]

    response = Response(
        answer=answer,
        class_1=class_1,
        class_2=class_2
    )
    return response


@app.post("/classify")
async def predict_class(request: Request) -> ResponseClassify:
    result_one = onnx_clf_one(request.question)
    class_1=id2label_one[result_one[0]['label'].split('_')[1]]
    result_two = onnx_clf_two(request.question)
    class_2=id2label_two[result_two[0]['label'].split('_')[1]]

    return {'class_1': class_1,
     'answer_1': result_one[0],
     'class_2': class_2,
     'answer_2': result_two[0]}


if __name__ == "__main__":
    uvicorn.run(app="__main__:app", log_level="debug", host="0.0.0.0")
