import uvicorn
from fastapi import FastAPI

from src.rag.main import rag_pipeline
from src.rag.retriever import create_chroma_db, get_collection
from src.classifier import onnx_clf_one, onnx_clf_two, id2label_one, id2label_two
from .schema import Request, Response

create_chroma_db()

collection = get_collection()

app = FastAPI()

@app.get("/")
def index():
    return {"text": "Интеллектуальный помощник оператора службы поддержки."}


@app.post("/predict")
async def get_reponse(request: Request) -> Response:
    result_one = onnx_clf_one(request.question)
    result_two = onnx_clf_two(request.question)

    response = Response(
        answer=rag_pipeline(input=request.question,collection=collection)["actual_response"],
        class_1=id2label_one[result_one[0]["label"].split("_")[1]],
        class_2=id2label_two[result_two[0]["label"].split("_")[1]],
    )
    return response


@app.post("/classify")
async def predict_class(request: Request) -> Response:
    result_one = onnx_clf_one(request.question)
    result_two = onnx_clf_two(request.question)

    response = Response(
        answer="", 
        class_1=id2label_one[result_one[0]["label"].split("_")[1]],
        class_2=id2label_two[result_two[0]["label"].split("_")[1]],
    )
    return response


if __name__ == "__main__":
    uvicorn.run(app="__main__:app", log_level="debug", host="0.0.0.0")
