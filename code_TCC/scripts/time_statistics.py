import os
import csv
import pandas as pd
import numpy as np
from datetime import datetime

from code_TCC.scripts import utils

csv_path = utils.CSV_FILES_FOLDER

movements = utils.movements
sequence = utils.sequence
expected_joint_angles = utils.expected_joint_angles

indexes = ['Date', 'Movement', 'Actuator', 'Mode', 'Min', 'Max', 'Mean', 'Median', 'Standard Deviation']


def calculate_mean(data: list):
    return sum(data) / len(data)


def calculate_median(data: list):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    return median


def calculate_standard_deviation(data: list):
    return np.std(data)


def calculate_mode(data: list):
    modes = {}
    for instance in data:
        if instance not in modes:
            modes[i] = 1
        else:
            modes[i] += 1

    return [mode for mode, count in modes.items() if count == max(modes.values())]


time_variation = []
time_statistics = []
csv_time_statistics = []

for directory in os.listdir(csv_path):
    for file in os.listdir(f'{csv_path}/{directory}'):
        with open(f'{csv_path}/{directory}/{file}', 'r') as csv_file:
            dataframe = pd.read_csv(csv_file)

            date = f'{directory}'
            actuator = f'{file}'
            # index = int(actuator.split("_")[1])

            for movement in list(movements.keys()):
                filtered_df = dataframe[dataframe['Movement'] == movement]

                time_instances = filtered_df['Time'].tolist()

                for i in range(len(time_instances)):
                    variation = datetime.strptime(time_instances[i + 1], "%H:%M:%S") - datetime.strptime(
                        time_instances[i], "%H:%M:%S") if i < len(time_instances) - 1 \
                        else datetime.strptime(time_instances[i - 1], "%H:%M:%S") - datetime.strptime(
                        time_instances[i - 2], "%H:%M:%S")

                    time_variation.append(variation.seconds)

                time_statistics = [date, movement, actuator, calculate_mode(time_variation)[0], min(time_variation),
                                   max(time_variation), calculate_mean(time_variation),
                                   calculate_median(time_variation), calculate_standard_deviation(time_variation)]

                csv_time_statistics.append(time_statistics)

with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/time_statistics_between_movements.csv', 'w',
          newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(indexes)
    for row in csv_time_statistics:
        csv_writer.writerow(row)
