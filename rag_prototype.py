from pprint import pprint
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

loader = DirectoryLoader("./rutube/rutube_hackathon/data/from_site/md",
                         glob="**/*.md",
                         show_progress=True)
docs = loader.load()

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
splits = [markdown_splitter.split_text(document.page_content) for document in docs]
#

chunk_size = 512
chunk_overlap = 50
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

splits = [text_splitter.split_documents(md_header_splits) for md_header_splits in splits]

splits = [document for sublist in splits for document in sublist]

db = Chroma.from_documents(splits,
                           HuggingFaceEmbeddings(model_name="embaas/sentence-transformers-multilingual-e5-base"))

retriever = db.as_retriever()



pprint(db.similarity_search(query='А как с YouTube что-то перетащить?'))