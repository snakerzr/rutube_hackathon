DEVICE = 'cuda'
CHROMA_DB_PATH = '../data/chroma_db'
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
DATA_FOR_DB_PARQUET = 'data/actual/interim/data_for_db_corrected.parquet'
# EVALUATION_PARQUET = '../data/actual/interim/evaluation_df.parquet'
# SMALL_EVALUATION_PARQUET = '../data/actual/interim/evaluation_df_125.parquet'


CLASSIFIER_ONE = "../../zve-data/clf_one_opt"
CLASSIFIER_TWO = "../../zve-data/clf_two_opt"

ID2LABEL_ONE = "../../zve-data/if2label_one.json"
ID2LABEL_TWO = "../../zve-data/id2label_two.json"


RAG_API_ENDPOINT = 'http://localhost:8000/predict'
CLASSIFICATOR_ENDPOINT = 'http://localhost:8000/classify'