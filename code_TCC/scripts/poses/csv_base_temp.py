import os
import csv
import json

from code_TCC.scripts.utils import actuator_utils as utils

json_files_path = utils.JSON_FILES_FOLDER_PATH
csv_files_path = utils.CSV_FILES_FOLDER

for file in os.listdir(json_files_path):
    with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/json_data_files/{file}', 'r') as json_file:
        json_data = json.load(json_file)

        instances = list(json_data.keys())

        data = [['instance', 'temperatureCpu']]

        for count, instance in enumerate(instances):
            feedback_robot = json_data[instance][1]

            parsed_data = json.loads(feedback_robot)

            base_data = parsed_data['base']

            data.append([instance, base_data['temperatureCpu']])

    with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/poses/temperatureCPU/{file.split(".")[0]}.csv', 'w', newline = '') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            csv_writer.writerow(row)
