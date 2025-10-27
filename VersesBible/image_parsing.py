import time
import requests

from VersesBible.config import KEY

url = f'https://api.unsplash.com/photos/random'

headers = {
    "Authorization": f"Client-ID {KEY}",
}
params = {
    'query': "nature",
    'count': 30
}

usr_ids = set()

total = 404
cnt = 163
while cnt <= total:
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        for j, photo in enumerate(data):
            photo_id = photo['id']
            if photo_id in usr_ids:
                continue
            else:
                usr_ids.add(photo_id)
            photo_url = photo['urls']['full'] + "&w=1080&h=1080&fit=crop"
            response = requests.get(photo_url, stream=True)
            with open(rf"/home/jk-n/Pictures/VersesBible/image{cnt}.jpg", "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            print(f"{cnt}/{total} Скачано: image_{cnt}.jpg")
            cnt += 1
            time.sleep(3)

    except Exception as e:
        print("Ошибка: ", e)
        time.sleep(3600)
