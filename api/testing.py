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

print(json['access_token'])

# print(response.status_code)
# print(response.json()))