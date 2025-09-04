from VersesBible.config import KEY
import requests

query = "nature"
count = 10


url = f'https://api.unsplash.com/search/photos'
params = {
    'query': query,
    'per_page': count,
    'client_id': KEY,
}

response = requests.get(url, params=params)
photos = response.json()
print(photos)