from services.rag_service import RagService
from services.flow_service import FlowService

# PDF parsing
file_path = (
    "contract_example.pdf"
)

original_prompt = "Tell me about the Debtor"

rag = RagService()
rag.parse_doc(file_path)

enhanced_prompt = rag.enhance_prompt(original_prompt)

flow = FlowService()

response = flow.chat_completions(enhanced_prompt)

print(response)
