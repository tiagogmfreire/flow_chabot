class ChatService:

    def __init__(self, rag_service, flow_service, file_path = "uploaded_files/rag.pdf"):
        self.rag_service  = rag_service
        self.flow_service = flow_service
        self.file_path    = file_path
    
    def chat(self, prompt):
        # self.rag_service.parse_doc(self.file_path)
        enhanced_prompt = self.rag_service.enhance_prompt(prompt)

        response = self.flow_service.chat_completions(enhanced_prompt)

        return response