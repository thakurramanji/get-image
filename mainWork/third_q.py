

import os

import requests

base_url = 'https://picsum.photos/'


end_point = base_url + 'v2/list?page=1?limit=100'

response = requests.get(end_point)

data = response.json()

for img in data:
    img_url = img["url"]
    width = img["width"]
    height = img["height"]
    print(f"Url: {img_url}")
    print(f"before resize:{width}*{height} ")
    print(f"after resize: 2048*{height}\n")