import chromadb
import pandas as pd
import requests

from config import CHROMA_DB_PATH, CLASSIFICATOR_ENDPOINT, DATA_FOR_DB_PARQUET
from rag.embedder import embedder


def create_chroma_db(persistant_path: str = CHROMA_DB_PATH):
    data_for_db = pd.read_parquet(DATA_FOR_DB_PARQUET)

    client = chromadb.PersistentClient(
        path=persistant_path, settings=chromadb.Settings(allow_reset=True)
    )
    client.reset()

    collection = client.get_or_create_collection(
        name="rutube", metadata={"hnsw:space": "cosine"}
    )

    documents = data_for_db["kb_query"].tolist()
    documents_query = ["query: " + doc for doc in documents]

    embeddings = embedder.encode(documents_query, show_progress_bar=True)

    metadatas = data_for_db.drop(columns=["index", "kb_query"]).to_dict(orient="index")
    metadatas = [data[1] for n, data in enumerate(metadatas.items())]

    ids = [str(x) for x in data_for_db["index"].tolist()]

    collection.add(
        documents=documents, embeddings=embeddings, metadatas=metadatas, ids=ids
    )


def get_collection() -> chromadb.Collection:
    client = chromadb.PersistentClient(
        path=CHROMA_DB_PATH, settings=chromadb.Settings(allow_reset=True)
    )
    collection = client.get_or_create_collection(
        name="rutube", metadata={"hnsw:space": "cosine"}
    )
    return collection


def retrieve_relevant_chunks(
    collection: chromadb.Collection,
    query: str | list[str],
    where: dict | None = None,
    where_document: dict | None = None,
    n_results: int = 3,
) -> None:
    """
    where={"metadata_field": "is_equal_to_this"},
    where_document={"$contains":"search_string"}
    """

    if isinstance(query, str):
        query = [query]

    query = ["query: " + q for q in query]

    query_embeddings = embedder.encode(query)

    query_kwargs = {
        "query_embeddings": query_embeddings,
        "include": ["documents", "metadatas"],
        "n_results": n_results,
    }
    if where:
        query_kwargs["where"] = where

    if where_document:
        query_kwargs["where_document"] = where_document

    result = collection.query(**query_kwargs)
    return result


def format_retrieve_result(retrieve_result: dict) -> list:
    result = []

    ids = retrieve_result.get("ids", [])
    documents = retrieve_result.get("documents", [])
    metadatas = retrieve_result.get("metadatas", [])

    for i in range(len(ids)):
        group = []
        for j in range(len(ids[i])):
            entry = {
                "id": ids[i][j],
                "document": documents[i][j],
                "metadata": metadatas[i][j] if metadatas else None,
            }
            group.append(entry)
        result.append(group)

    return result


def extract_context_for_generation(
    retrieved_result: list[dict], include_question: bool = True
) -> str:
    result_string = "\n\n".join(
        [
            (
                f"Вопрос: {item['document']}\nОтвет: {item['metadata']['kb_answer']}"
                if include_question
                else item["metadata"]["kb_answer"]
            )
            for sublist in retrieved_result
            for item in sublist
        ]
    )
    return result_string


def classify(question: str) -> str:
    response = requests.post(CLASSIFICATOR_ENDPOINT, json={"question": question})
    return response.json()["class_1"], response.json()["class_2"]
