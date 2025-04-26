import os

import requests

base_url = 'https://picsum.photos/'


end_point = base_url + 'v2/list'

response = requests.get(end_point)

data = response.json()
download_urls = []
ids = []

for d in data:
    t = {}

    t["download_url"] = d["download_url"]
    t["id"] = d['id']
    download_urls.append(t)

os.makedirs("img_dir")

for url in download_urls[:10]:
    image_id = url['id']
    img_url = url["download_url"]

    image_data = requests.get(img_url)

    with open(f'img_dir/{image_id}.jpg', 'wb') as f:
        f.write(image_data.content)

    print(f'Downloaded {image_id}.jpg')