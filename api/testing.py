from services.rag_service import RagService
from services.flow_service import FlowService
from models.vector_model import VectorModel
import sys

# PDF parsing
file_path = (
    "uploaded_files/contract_example.pdf"
)

original_prompt = sys.argv[1]

vector = VectorModel()

rag = RagService(vector)
rag.parse_doc(file_path)

enhanced_prompt = rag.enhance_prompt(original_prompt)

flow = FlowService()

response = flow.chat_completions(enhanced_prompt)

print(response)
