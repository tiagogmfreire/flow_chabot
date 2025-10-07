import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

response = requests.get(
    str(base_url + "/ai-orchestration-api/v1/health")
)

print(response.status_code)
print(response.text)