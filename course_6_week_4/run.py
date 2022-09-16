#! /usr/bin/env python3

import os
import requests

url = "http://localhost/fruits/"

dir_txt = "supplier-data/descriptions/"
description_files = os.listdir(dir_txt)

fields = ['name', 'weight', 'description']
for file in description_files:
    with open(dir_txt + file, "r") as f:
        text = f.read().split('\n')
        image_data = dict(zip(fields, text))

        image_data['weight'] = int(image_data['weight'][:-4])
        image_data['image_name'] = file.replace(".txt", ".jpeg")

        response = requests.post(url, data=image_data)
        if response.status_code == 201:
            print(f"Request was succeeded: image {file} uploaded")
        else:
            print("Response: ", response.status_code)
