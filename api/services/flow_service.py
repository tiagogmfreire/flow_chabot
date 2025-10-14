import requests
import json
import os

class FlowService:

    def generate_token(self):

        import os
        import json
        import requests

        from dotenv import load_dotenv

        load_dotenv()

        base_url = os.getenv("BASE_URL")
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")

        headers = {
            'accept'       : '/',
            'Content-Type' : 'application/json',
            'FlowTenant'   : 'Stretto',
        }

        payload = {
            'clientId'      : client_id,
            'clientSecret'  : client_secret,
            'appToAccess'   : "llm-api"
        }

        url = str(base_url + "/auth-engine-api/v1/api-key/token")

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        json = response.json()

        return json['access_token']
    
    def chat_completions(self, prompt):

        token = self.generate_token()

        payload = {
          "stream": False,
          "max_tokens": 4096,
          "temperature": 0.7,
          "allowedModels": [
            "gpt-4o-mini"
          ],
          "messages": [
            {
              "role": "user",
              "content": prompt
            }
          ]
        }

        url = str(os.getenv("BASE_URL") + "/ai-orchestration-api/v1/openai/chat/completions")

        headers = {
            "Authorization": str("Bearer " + token),
            'Content-Type' : 'application/json',
            "FlowTenant": "Stretto",
            "FlowAgent": "default-agent"
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        body = response.json()

        return body