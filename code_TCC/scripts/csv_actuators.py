import os
import csv
import json

JSON_FILES_FOLDER_PATH = "C:/Users/jams/Documents/Pessoal/code_TCC/json_data_files"
CSV_FILES_FOLDER = "C:/Users/jams/Documents/Pessoal/code_TCC/csv_data_files"

actuators = ['actuator_1', 'actuator_2', 'actuator_3', 'actuator_4', 'actuator_5', 'actuator_6']

actuator_attributes = ['commandId', 'statusFlags', 'jitterComm', 'position', 'velocity', 'torque',
                       'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore', 'faultBankA',
                       'faultBankB', 'warningBankB', 'warningBankB']

actuator_attributes_csv = ['Time', 'Movement', 'commandId', 'statusFlags', 'jitterComm', 'position', 'velocity',
                           'torque',
                           'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore', 'faultBankA', 'faultBankB',
                           'warningBankB', 'warningBankB']

actuator_attributes_interest = ['jitterComm', 'position', 'velocity', 'torque',
                                'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore']

actuator_dict = {}

for file in os.listdir(JSON_FILES_FOLDER_PATH):
    with open(f'{JSON_FILES_FOLDER_PATH}/{file}', 'r') as json_file:
        json_data = json.load(json_file)

        date = file.split(".")[0]

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

    if not os.path.isdir(f'{CSV_FILES_FOLDER}/{date}'):
        os.mkdir(f'{CSV_FILES_FOLDER}/{date}')
        for actuator in actuators:
            with open(f'{CSV_FILES_FOLDER}/{date}/{actuator}', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(actuator_attributes_csv)
                for row in actuator_dict[actuator].values():
                    csv_writer.writerow(row)
    else:
        pass

    actuator_dict.clear()
