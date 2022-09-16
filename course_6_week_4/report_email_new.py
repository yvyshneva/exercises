#!/usr/bin/env python3

import datetime
import os
import reports
import emails


def process_data(directory):
    files = os.listdir(directory)

    all_data = ""
    for file in files:
        with open(directory + file, "r") as f:
           text = f.read().split("\n")[:2]
           data = [f'name: {text[0]}',
                   f'weight: {text[1]}',
                   "<br/>"]
           #print("\n".join(data))
           all_data += "<br/>".join(data)
    #print(all_data)
    return all_data

today = datetime.date.today()

if __name__ == "__main__":
    data = process_data("supplier-data/descriptions/")
    title = f"Processed Update on {today}"
    reports.generate_report('/tmp/processed.pdf', title, data)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
