import os

import requests

base_url = 'https://picsum.photos/'

page = 1
#end_point = base_url + 'v2/list?page=1&limit=100'

mapp={}

while True:
    url = f"{base_url}v2/list?page={page}&limit=100"

    response = requests.get(url)
    data = response.json()

    # idd =  data.get('id',[])

    if not data:
        break

    for d in data:
        author = d["author"]
        if author not in mapp:
            mapp[author]=1
        else:
            mapp[author] += 1

    page+=1


print(len(mapp))

print(mapp)