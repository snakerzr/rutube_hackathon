from sentence_transformers import SentenceTransformer

from config import DEVICE

embedder = SentenceTransformer("intfloat/multilingual-e5-large", device=DEVICE)
