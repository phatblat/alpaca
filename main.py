import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('BASE_URL')
print(f'Alpaca API base URL: {base_url}')
api_key_id = os.getenv('API_KEY_ID')
print(f'Alpaca API key ID: {api_key_id}')
secret_key = os.getenv('SECRET_KEY')
print(f'Alpaca API secret key: {secret_key}')

api_url = f"{base_url}/v2/account"
session = requests.Session()
session.headers.update({
    'APCA-API-KEY-ID': api_key_id,
    'APCA-API-SECRET-KEY': secret_key,
})

response = requests.get(api_url)
print(response.status_code)
data = response.json()
print(data)
