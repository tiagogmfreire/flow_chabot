from langchain_community.document_loaders import PyPDFLoader

file_path = (
    "contract_example.pdf"
)

loader = PyPDFLoader(file_path)
pages = []

for page in loader.lazy_load():
    pages.append(page)

print(f"{pages[0].metadata}\n")
print(pages[0].page_content)