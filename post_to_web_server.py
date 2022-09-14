
#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback"
feedback_files = os.listdir(dir)
feedbacks = []

feedback_fields = ['title', 'name', 'date', 'feedback']
for file in feedback_files:
    with open(dir + "/" + file, "r") as f:
        text = f.read().split('\n')
        feedback = dict(zip(feedback_fields, text))
        response = requests.post("http://34.133.0.120/feedback/", data=feedback)
        if response.status_code == 201:
            print("Request was succeeded")
        else:
            print("Response: ", response.status_code)
