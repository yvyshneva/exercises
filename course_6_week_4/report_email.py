#!/usr/bin/env python3

import datetime
import os
import reports


def process_data(directory):
    files = os.listdir(directory)

    all_data = []
    for file in files:
        with open(directory + file, "r") as f:
           text = f.read().split("\n")[:2]
           data = [f'name: {text[0]}',
                   f'weight: {text[1]}',
                   "\n"]
           all_data += data
    return all_data

today = date.today()

if __name__ == "__main__":
    data = process_data("supplier-data/descriptions/")
    title = f"Processed Update on {today}"
    reports.generate_report('/tmp/processed.pdf', title, "", "/n".join(data))
