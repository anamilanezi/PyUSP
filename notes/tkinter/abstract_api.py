import tkinter as tk
import json
import requests
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from pprint import pprint

from random import choice

URL = "http://shibe.online/api/shibes"
parameters = {
    "count": 20,
}

response = requests.get(URL, params=parameters)
print(response.status_code)

images_list = response.json()

# ------ Resize image from URL ------ #
params = {
    "width": 250,
    "height": 250,
    "strategy": 'auto',
}

data = {
    "api_key": '2fd4b30c69604181aa5e83ebc98e0f93',
    "url": choice(images_list),
    "lossy": True,
    "resize": params,
    }

request = Request(
    'https://images.abstractapi.com/v1/url/',
    data=json.dumps(data).encode('ascii'),
    headers={"Content-Type": 'application/json'},
    method='POST',
    )

with urlopen(request) as response:
    image = json.load(response)['url']
    print(image)





