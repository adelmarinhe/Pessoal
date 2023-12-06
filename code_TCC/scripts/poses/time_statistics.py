import os
from datetime import datetime

import matplotlib.pyplot as plt

import pandas as pd

from code_TCC.scripts.utils.base_utils import commanded_positions_dict

from code_TCC.scripts.utils.actuator_utils import positions

commanded_positions = commanded_positions_dict

path = f'C:/Users/jams/Documents/Pessoal/code_TCC/csv_data_files/base'
save_path = f'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/poses/time_histograms'

positions = positions

indexes = ['a)', 'b)', 'c)']

for j, file in enumerate(os.listdir(path)):
    time_variation = []
    # print(indexes[i])
    # print(i)
    with open(f'{path}/{file}', 'r') as csv_file:
        dataframe = pd.read_csv(csv_file)

        # for position in positions:
        filtered_dataframe = dataframe[dataframe['Position'] == 'position_1']
        instances = filtered_dataframe['Time'].tolist()

        for i in range(len(instances)):
            variation = datetime.strptime(instances[i + 1], "%H:%M:%S") - datetime.strptime(
                instances[i], "%H:%M:%S") if i < len(instances) - 1 \
                else datetime.strptime(instances[i - 1], "%H:%M:%S") - datetime.strptime(
                instances[i - 2], "%H:%M:%S")

            time_variation.append(variation.seconds)

    plt.hist(time_variation, bins=15, edgecolor='black', linewidth=0.8)
    plt.title(f'{indexes[j]} {file.split(".")[0]}')
    plt.xlabel('Time [in seconds]')
    plt.ylabel('Frequency')

    plt.savefig(f'{save_path}/{file.split(".")[0]}.png')

    plt.close()