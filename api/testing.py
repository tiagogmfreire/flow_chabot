import os
import jwt
from dotenv import load_dotenv

load_dotenv()

token = jwt.encode({"some": "payload"}, os.getenv("API_KEY"), algorithm="HS256")

print(token)