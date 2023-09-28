import os
import csv
import pandas as pd
import numpy as np

from code_TCC.scripts import utils

csv_path = utils.CSV_FILES_FOLDER

movements = utils.movements
sequence = utils.sequence
expected_joint_angles = utils.expected_joint_angles

indexes = ['Date', 'Movement', 'Actuator', 'Expected Value', 'Mean', 'Median', 'Standard Deviation']


def calculate_mean(data: list):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        # Average of the middle two elements for an even-sized list
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    return median


def calculate_standard_deviation(data):
    # Calculate the standard deviation using numpy
    return np.std(data)


parameter = 'position'

means = []
csv_means = []

for directory in os.listdir(csv_path):
    for file in os.listdir(f'{csv_path}/{directory}'):
        with open(f'{csv_path}/{directory}/{file}', 'r') as csv_file:
            dataframe = pd.read_csv(csv_file)

            date = f'{directory}'
            actuator = f'{file}'
            index = int(actuator.split("_")[1])

            for movement in movements:
                filtered_df = dataframe[dataframe['Movement'] == movement]

                positions = filtered_df[parameter].tolist()

                means = [date, movement, actuator, expected_joint_angles[movement][index - 1],
                         calculate_mean(positions), calculate_median(positions),
                         calculate_standard_deviation(positions)]

                csv_means.append(means)

    with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/mean_{parameter}_by_movement.csv', 'w',
              newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(indexes)
        for row in csv_means:
            csv_writer.writerow(row)
