import os
import csv
import json

from code_TCC.scripts import utils

json_files_path = utils.JSON_FILES_FOLDER_PATH
csv_files_path = utils.CSV_FILES_FOLDER

actuators = ['actuator_1', 'actuator_2', 'actuator_3', 'actuator_4', 'actuator_5', 'actuator_6']

actuator_attributes = utils.actuator_attributes

actuator_attributes_csv = ['Time', 'Movement', 'commandId', 'statusFlags', 'jitterComm', 'position', 'velocity',
                           'torque', 'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore', 'faultBankA',
                           'faultBankB', 'warningBankB', 'warningBankB']

actuator_attributes_interest = ['jitterComm', 'position', 'velocity', 'torque',
                                'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore']

movements_dict = utils.movements

inverse_movement = {value: key for key, value in movements_dict.items()}

movements = utils.sequence

actuator_dict = {}

for file in os.listdir(json_files_path):
    with open(f'{json_files_path}/{file}', 'r') as json_file:
        json_data = json.load(json_file)

        date = file.split(".")[0]

        instances = list(json_data.keys())
    for count, instance in enumerate(instances):
        movement = json_data[instance][0]

        # movement = f"movement_{(count % 7) + 1}"

        if movement == 'Home' and count % 7 == 0:
            movement = 'movement_1'
        elif movement == 'movement_2_safe_grasp' and count % 7 in [1, 3]:
            movement = f"movement_{(count % 7) + 1}"
        elif movement == 'movement_3_grasp' and count % 7 == 2:
            movement = 'movement_3'
        elif movement == 'movement_4_safe_release' and count % 7 in [4, 6]:
            movement = f"movement_{(count % 7) + 1}"
        elif movement == 'movement_5_release' and count % 7 == 5:
            movement = 'movement_6'
        else:
            # raise ValueError(f"Erro fodaci linha {count+1}")
            print(f"Erro fodaci linha {count+1}")

        feedback_robot = json_data[instance][1]

        parsed_data = json.loads(feedback_robot)

        actuator_data = parsed_data['actuators']

        for i, actuator in enumerate(actuators):
            if actuator not in actuator_dict:
                actuator_dict[actuator] = {}
            actuator_dict[actuator][count] = [instance, movement]
            feedback_attributes = list(actuator_data[i].keys())

            for attribute in actuator_attributes:
                actuator_dict[actuator][count].append(actuator_data[i][attribute]) \
                    if attribute in feedback_attributes else actuator_dict[actuator][count].append(" ")

    if not os.path.isdir(f'{csv_files_path}/{date}'):
        os.mkdir(f'{csv_files_path}/{date}')
        for actuator in actuators:
            with open(f'{csv_files_path}/{date}/{actuator}', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(actuator_attributes_csv)
                for row in actuator_dict[actuator].values():
                    csv_writer.writerow(row)
    else:
        pass

    actuator_dict.clear()
