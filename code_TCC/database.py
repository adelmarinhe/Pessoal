import pandas as pd
import json
import os

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"

for file in os.listdir(JSON_FILES_FOLDER):
    print(file)
    df = pd.read_json(file)
    df.to_csv(f'{CSV_FILES_FOLDER}/{file}.csv')

print(df)