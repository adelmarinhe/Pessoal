import csv
import os
import pandas as pd
import numpy as np

path_csv = 'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/poses/diff_norm/'
path_save = 'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/poses/boxplots/'

for directory in os.listdir(path_csv):
    data = []
    for i, file in enumerate(os.listdir(f'{path_csv}/{directory}')):
        date = f'{directory}'
        with open(f'{path_csv}/{directory}/{file}', 'r') as csv_file:
            dataframe = pd.read_csv(csv_file)
            errors = dataframe['error_vector'].tolist()

            data.append([f'Position {i+1}', np.mean(errors), np.std(errors), np.max(errors), np.min(errors)])

        with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/poses/means/statistics_test_{directory}.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Position', 'Mean', 'Std_Dev', 'Max', 'Min'])
            for row in data:
                csv_writer.writerow(row)
