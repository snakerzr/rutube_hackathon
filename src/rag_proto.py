import requests

import pandas as pd

from sentence_transformers import SentenceTransformer

import chromadb

OLLAMA_ENDPOINT = "http://89.169.135.235:11434/api/generate"

DEVICE = 'cuda'
CHROMA_DB_PATH = '../data/chroma_db'
DATA_FOR_DB_PARQUET = '../data/actual/interim/data_for_db_corrected.parquet'
# EVALUATION_PARQUET = '../data/actual/interim/evaluation_df.parquet'
# SMALL_EVALUATION_PARQUET = '../data/actual/interim/evaluation_df_125.parquet'

## Data for db
data_for_db = pd.read_parquet(DATA_FOR_DB_PARQUET)
# data_for_db = data_for_db.fillna('')

## Embedder
embedder = SentenceTransformer('intfloat/multilingual-e5-large',device=DEVICE)

## Database
client = chromadb.PersistentClient(path=CHROMA_DB_PATH, settings=chromadb.Settings(allow_reset=True))
client.reset()
collection = client.get_or_create_collection(name="rutube",metadata={"hnsw:space": "cosine"})
documents = data_for_db['kb_query'].tolist()
documents_query = ['query: ' + doc for doc in documents]
embeddings = embedder.encode(documents_query, show_progress_bar=True)
metadatas = data_for_db.drop(columns=['index','kb_query']).to_dict(orient='index')
metadatas = [data[1] for n,data in enumerate(metadatas.items())]
ids = [str(x) for x in data_for_db['index'].tolist()]
collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

## Retriever
def retrieve_relevant_chunks(query:str | list[str], where: dict | None = None, where_document: dict | None = None, n_results:int = 3) -> None:
    '''
    where={"metadata_field": "is_equal_to_this"},
    where_document={"$contains":"search_string"}
    '''

    if isinstance(query,str):
        query=[query]

    query = ['query: ' + q for q in query]
        
    query_embeddings = embedder.encode(query)

    query_kwargs = {
        'query_embeddings': query_embeddings,
        'include': ['documents','metadatas'],
        'n_results': n_results
    }
    if where:
        query_kwargs['where']=where

    if where_document:
        query_kwargs['where_document'] = where_document

    result = collection.query(**query_kwargs)
    return result

def format_retrieve_result(retrieve_result) -> list:
    result = []

    ids = retrieve_result.get('ids', [])
    documents = retrieve_result.get('documents', [])
    metadatas = retrieve_result.get('metadatas', [])

    for i in range(len(ids)):
        group = []
        for j in range(len(ids[i])):
            entry = {
                'id': ids[i][j],
                'document': documents[i][j],
                'metadata': metadatas[i][j] if metadatas else None
            }
            group.append(entry)
        result.append(group)

    return result

def extract_context_for_generation(retrieved_result: list[dict], include_question: bool = True) -> str:
    result_string = "\n\n".join(
        [
            (f"Вопрос: {item['document']}\nОтвет: {item['metadata']['kb_answer']}" if include_question else item['metadata']['kb_answer'])
            for sublist in retrieved_result for item in sublist
        ]
    )
    
    return result_string

## Generation
def generate(prompt:str, temperature:float=0, return_str_only:bool=True) -> dict:
    result = requests.post(
        OLLAMA_ENDPOINT,
        json={
            "model": "mistral-nemo",
            "options": {"seed": 123, "temperature": temperature},
            "prompt": prompt,
            "stream": False,
        },
    ).json()
    if return_str_only:
        return result['response']
    else:
        return result
    
## Chunk LLM filtering prompt (optional)
FILTERING_PROMPT = '''
'''.strip()
def chunk_filtering(input:str,query:str) -> bool:
    pass

## Prompt template
PROMPT_TEMPLATE = '''
Ты интеллектуальный помощник службы поддержки RUTUBE. 
RUTUBE — ведущий российский видеопортал, предлагающий к просмотру тв онлайн, кинофильмы, сериалы, мультфильмы и пользовательское видео.
Ты очень вежливый и дружелюбный. Твоя задача ответить на ВОПРОС используя КОНТЕКСТ. 

У тебя есть только знания из контекста и этого промпта.
Если ответа на вопрос к контексте нет, то напиши, что не знаешь ответа.
Отвечай только используя контекст, не используй другие знания.

ВОПРОС:
=====
{query}
=====

КОНТЕКСТ:
=====
{context}
=====
'''.strip()

## Complete QA-RAG pipeline
def rag_pipeline(input:str) -> dict:
    actual_context_raw = retrieve_relevant_chunks(input,n_results=5)
    actual_context = format_retrieve_result(actual_context_raw)
    actual_context_to_llm = extract_context_for_generation(actual_context)
    prompt = PROMPT_TEMPLATE.format(query=input,context=actual_context_to_llm)
    response = generate(prompt)


    result = {
        'input':input,
        'actual_context': actual_context,
        'actual_response': response
    }

    return result

# rag_pipeline('Как включить монетизацию?')