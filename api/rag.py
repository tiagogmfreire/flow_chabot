from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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

print(f"Split file {len(all_splits)} sub-documents.")