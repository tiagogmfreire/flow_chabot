from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class RagService:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    def parse_doc(self, file_path):

        if not os.path.exists(file_path):
            return []

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

        snippets = self.vector_store.similarity_search(original_prompt)

        if not snippets: 
            return original_prompt

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