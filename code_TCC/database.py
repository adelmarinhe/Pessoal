import pandas as pd
import json
import os

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"

for file in os.listdir(JSON_FILES_FOLDER):
    with open(f'{JSON_FILES_FOLDER}/{file}', 'r') as json_file:
        data = json.load(json_file)

instances = list(data.keys())

# for instance in instances:
#     data_edit = data[instance].split('}')
#     # base_data = [base[]
#     print(data_edit)

data_edit = data[instances[3]].split(' ' and '\n')

print(data_edit)