import json

from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

from config import CLASSIFIER_ONE, CLASSIFIER_TWO, ID2LABEL_ONE, ID2LABEL_TWO

tokenizer = AutoTokenizer.from_pretrained(CLASSIFIER_ONE)

clf_one = ORTModelForSequenceClassification.from_pretrained(
    CLASSIFIER_ONE
)
clf_two = ORTModelForSequenceClassification.from_pretrained(
    CLASSIFIER_TWO
)

onnx_clf_one = pipeline("text-classification", model=clf_one, tokenizer=tokenizer)
onnx_clf_two = pipeline("text-classification", model=clf_two, tokenizer=tokenizer)

with open(ID2LABEL_ONE, "r") as json_file:
    id2label_one = json.load(json_file)

with open(ID2LABEL_TWO, "r") as json_file:
    id2label_two = json.load(json_file)