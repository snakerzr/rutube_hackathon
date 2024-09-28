import json

from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification

from fastapi import FastAPI

import uvicorn

from pydantic import BaseModel

from src.rag_proto import rag_pipeline

class Request(BaseModel):
    question: str


class Response(BaseModel):
    answer: str
    class_1: str
    class_2: str


tokenizer = AutoTokenizer.from_pretrained('../../zve-data/clf_one_opt')

clf_one = ORTModelForSequenceClassification.from_pretrained('../../zve-data/clf_one_opt')
clf_two = ORTModelForSequenceClassification.from_pretrained('../../zve-data/clf_two_opt')

onnx_clf_one = pipeline("text-classification", model=clf_one, tokenizer=tokenizer)
onnx_clf_two = pipeline("text-classification", model=clf_two, tokenizer=tokenizer)

with open('../../zve-data/if2label_one.json', 'r') as json_file:
    id2label_one = json.load(json_file)

with open('../../zve-data/id2label_two.json', 'r') as json_file:
    id2label_two = json.load(json_file)

app = FastAPI()

@app.get("/")
def index():
    return {"text": "Интеллектуальный помощник оператора службы поддержки."}


@app.post("/predict")
async def predict_sentiment(request: Request) -> Response:
    result_one = onnx_clf_one(request.question)
    result_two = onnx_clf_two(request.question)

    response = Response(
        answer=rag_pipeline(request.question)['actual_response'],
        class_1=id2label_one[result_one[0]['label'].split('_')[1]],
        class_2=id2label_two[result_two[0]['label'].split('_')[1]]
    )
    return response

@app.post("/classify")
async def predict_class(request: Request) -> Response:
    result_one = onnx_clf_one(request.question)
    result_two = onnx_clf_two(request.question)

    response = Response(
        answer="", # rag_pipeline(request.question)['actual_response'],
        class_1=id2label_one[result_one[0]['label'].split('_')[1]],
        class_2=id2label_two[result_two[0]['label'].split('_')[1]]
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app='__main__:app',
               log_level='debug',
               host='0.0.0.0')


