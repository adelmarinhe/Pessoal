import json
import os
import csv

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"

actuators = ['actuator_1', 'actuator_2', 'actuator_3', 'actuator_4', 'actuator_5', 'actuator_6']

actuator_attributes = ['commandId', 'statusFlags', 'jitterComm', 'position', 'velocity', 'torque',
                       'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore', 'faultBankA',
                       'faultBankB', 'warningBankB', 'warningBankB']

actuator_dict = {}

for file in os.listdir(JSON_FILES_FOLDER):
    with open(f'{JSON_FILES_FOLDER}/{file}', 'r') as json_file:
        json_data = json.load(json_file)

        instances = list(json_data.keys())

        for count, instance in enumerate(instances):
            movement = json_data[instance][0]
            json_string = json_data[instance][1]  # movement data

            parsed_data = json.loads(json_string)  # feedback data

            actuator_data = parsed_data['actuators']  # list of dictionaries of the date

            for i, actuator in enumerate(actuators):
                if actuator not in actuator_dict:
                    actuator_dict[actuator] = {}
                actuator_dict[actuator][count] = [instance, movement]
                feedback_attributes = list(actuator_data[i].keys())

                for attribute in actuator_attributes:
                    actuator_dict[actuator][count].append(actuator_data[i][attribute]) \
                        if attribute in feedback_attributes else actuator_dict[actuator][count].append(" ")

    print(actuator_dict)
    for actuator in actuators:
        with open(f'{file}_{actuator}', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in actuator_dict[actuator].values():
                csv_writer.writerow(row)