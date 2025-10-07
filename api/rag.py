from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import init_chat_model
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from flow import generate_token
from dotenv import load_dotenv
import os

load_dotenv()

# PDF parsing
file_path = (
    "contract_example.pdf"
)

loader = PyPDFLoader(file_path)
pages = []

for page in loader.lazy_load():
    pages.append(page)

# print(f"{pages[0].metadata}\n")
# print(pages[0].page_content)

# splitting doc
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents(pages)

# print(f"Split file {len(all_splits)} sub-documents.")

flow_token = generate_token()

# print(flow_token)

# chat model
llm = init_chat_model(
    "gpt-4o-mini", 
    model_provider="azure-openai",
    azure_endpoint=os.getenv('BASE_URL'),
    openai_api_key=flow_token,
    api_version='3.0.0'
)

# print(llm)

# embeddings model
embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_base=os.getenv('BASE_URL'),
    openai_api_key=flow_token
)

# print(embeddings)

# vector store
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

# print(vector_store)

document_ids = vector_store.add_documents(documents=all_splits)

# print(document_ids)

# print(document_ids[:3])