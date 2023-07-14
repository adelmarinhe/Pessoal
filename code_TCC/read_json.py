import pandas as pd
with open('json_data_files/2023-07-13.json', 'r') as json_file:
    df = pd.read_json(json_file)
    df.to_csv('file.csv')
