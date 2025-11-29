#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data_list = []

        with open(csv_filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
