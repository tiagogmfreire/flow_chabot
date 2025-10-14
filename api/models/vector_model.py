from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class VectorModel:

    def __init__(self, collection_name="flow_rag", persist_directory="./chroma_langchain_db"):

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

        self.vector_store = Chroma(
            collection_name,
            embedding_function=embeddings,
            persist_directory="./chroma_langchain_db",
        )

    def add_documents(self, documents):

        document_ids = self.vector_store.add_documents(documents)

        return document_ids

    def similarity_search(self, query):

        chunks = self.vector_store.similarity_search(query)

        return chunks