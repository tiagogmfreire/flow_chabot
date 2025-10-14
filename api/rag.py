from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from services.flow_service import FlowService
from dotenv import load_dotenv
import requests
import json
import os
import sys

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

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

document_ids = vector_store.add_documents(documents=all_splits)

print(document_ids)

print(document_ids[:3])

# flow api request

original_prompt = "Tell me about the Debtor"

snippets = vector_store.similarity_search(original_prompt)

context = ""

for snippet in snippets:
    context += str(snippet.page_content + "\n\n")

enhanced_prompt = f"""
Use the following context to answer the user's question:

Context:
{context}

Original system instruction:
{original_prompt}
"""

flow = FlowService()

response = flow.chat_completions(enhanced_prompt)

print(response)
