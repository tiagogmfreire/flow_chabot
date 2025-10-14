from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class RagService:

    def __init__(self):

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

        self.vector_store = vector_store = Chroma(
            collection_name="example_collection",
            embedding_function=embeddings,
            persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
        )

    def parse_doc(self, file_path):

        loader = PyPDFLoader(file_path)
        pages = []

        for page in loader.lazy_load():
            pages.append(page)

        # print(f"{pages[0].metadata}\n")
        # print(pages[0].page_content)

        # splitting doc
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # chunk size (characters)
            chunk_overlap=200,  # chunk overlap (characters)
            add_start_index=True,  # track index in original document
        )

        all_splits = text_splitter.split_documents(pages)

        document_ids = self.vector_store.add_documents(documents=all_splits)

        return document_ids

    def enhance_prompt(self, original_prompt):

        original_prompt = "Tell me about the Debtor"

        snippets = self.vector_store.similarity_search(original_prompt)

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

        return enhanced_prompt