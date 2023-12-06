import csv
import os

import pandas as pd

from code_TCC.scripts.utils.base_utils import commanded_positions_dict

from code_TCC.scripts.utils.actuator_utils import positions

commanded_positions = commanded_positions_dict

path = f'C:/Users/jams/Documents/Pessoal/code_TCC/csv_data_files/base'
save_path = '/code_TCC/analyses/poses/diff_norm'

positions = positions


def calculate_norm(delta_x, delta_y, delta_z):
    return (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5


for file in os.listdir(path):
    with open(f'{path}/{file}', 'r') as csv_file:
        dataframe = pd.read_csv(csv_file)

        for position in positions:
            filtered_dataframe = dataframe[dataframe['Position'] == position]
            instances = filtered_dataframe['Time'].tolist()
            x = filtered_dataframe['tool_pose_x'].tolist()
            y = filtered_dataframe['tool_pose_y'].tolist()
            z = filtered_dataframe['tool_pose_z'].tolist()

            data = [['time', 'error_vector']]
            for i, instance in enumerate(instances):
                delta_x = x[i] - commanded_positions[position][0]
                delta_y = y[i] - commanded_positions[position][1]
                delta_z = z[i] - commanded_positions[position][2]

                norm = calculate_norm(delta_x, delta_y, delta_z)

                data.append([instance, norm])

                if not os.path.isdir(f'{save_path}/{file.split(".")[0]}'):
                    os.mkdir(f'{save_path}/{file.split(".")[0]}')

                with open(f'{save_path}/{file.split(".")[0]}/{position}.csv', 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    for row in data:
                        csv_writer.writerow(row)
