#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

dir = "supplier-data/images/"
images = os.listdir(dir)

for image in images:
  if "jpeg" not in image:
    continue
  with open(dir + image, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
