import os
import csv
import pandas as pd
import numpy as np

expected_joint_angles = {'Home': [0, 344, 75, 0, 300, 0],
                         'movement_2_safe_grasp': [22.690292358398438,
                                                   347.787841796875,
                                                   91.1580810546875,
                                                   345.40728759765625,
                                                   300.799072265625,
                                                   352.2476806640625],
                         'movement_3_grasp': [36.26722717285156,
                                              336.98724365234375,
                                              85.48641967773438,
                                              350.34735107421875,
                                              314.64813232421875,
                                              350.21044921875],
                         'movement_4_safe_release': [7.6923065185546875,
                                                     293.3585205078125,
                                                     36.652435302734375,
                                                     270.0581359863281,
                                                     283.05670166015625,
                                                     97.69122314453125],
                         'movement_5_release': [7.6994171142578125,
                                                288.1332702636719,
                                                38.8013916015625,
                                                270.02423095703125,
                                                290.4320068359375,
                                                97.71112060546875]}

JSON_FILES_FOLDER_PATH = "C:/Users/jams/Documents/Pessoal/code_TCC/json_data_files"
CSV_FILES_FOLDER = "C:/Users/jams/Documents/Pessoal/code_TCC/csv_data_files"
PLOTS_FOLDER = "C:/Users/jams/Documents/Pessoal/code_TCC/plots"

movements = ['movement_2_safe_grasp', 'movement_3_grasp', 'movement_4_safe_release', 'movement_5_release', 'Home']

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

for directory in os.listdir(CSV_FILES_FOLDER):
    for file in os.listdir(f'{CSV_FILES_FOLDER}/{directory}'):
        with open(f'{CSV_FILES_FOLDER}/{directory}/{file}', 'r') as csv_file:
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
