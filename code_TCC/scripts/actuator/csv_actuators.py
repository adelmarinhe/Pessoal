import os
import csv
import json

json_files_path = utils.JSON_FILES_FOLDER_PATH
csv_files_path = utils.CSV_FILES_FOLDER

actuators = ['actuator_1', 'actuator_2', 'actuator_3', 'actuator_4', 'actuator_5', 'actuator_6']

actuator_attributes = utils.actuator_attributes

dict_attributes = ['Time', 'Movement', 'commandId', 'statusFlags', 'jitterComm', 'position', 'velocity',
                   'torque', 'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore', 'faultBankA',
                   'faultBankB', 'warningBankB', 'warningBankB']

actuator_attributes_csv = ['position', 'velocity', 'torque', 'currentMotor', 'voltage',
                           'temperatureMotor', 'temperatureCore']

actuator_attributes_csv_write = ['Time', 'Movement', 'position', 'velocity', 'torque', 'currentMotor', 'voltage',
                                 'temperatureMotor', 'temperatureCore']

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

        if movement == 'Home' and count % 7 == 6:
            movement = f"movement_6"
        elif movement == 'movement_2_safe_grasp':
            if count % 7 == 0:
                movement = f"movement_7"
            elif count % 7 == 2:
                movement = f"movement_2"
        elif movement == 'movement_3_grasp' and count % 7 == 1:
            movement = f"movement_1"
        elif movement == 'movement_4_safe_release':
            if count % 7 == 3:
                movement = f"movement_3"
            elif count % 7 == 5:
                movement = f"movement_5"
        elif movement == 'movement_5_release' and count % 7 == 4:
            movement = f"movement_4"
        else:
            print(f"Error in {file}: line {count + 1}")

        feedback_robot = json_data[instance][1]

        parsed_data = json.loads(feedback_robot)

        actuator_data = parsed_data['actuators']

        for i, actuator in enumerate(actuators):
            if actuator not in actuator_dict:
                actuator_dict[actuator] = {}
            actuator_dict[actuator][count] = [instance, movement]
            feedback_attributes = list(actuator_data[i].keys())

            for attribute in actuator_attributes_csv:
                actuator_dict[actuator][count].append(actuator_data[i][attribute]) \
                    if attribute in feedback_attributes and attribute in actuator_attributes_csv else \
                    actuator_dict[actuator][count].append(" ")

    if not os.path.isdir(f'{csv_files_path}/{date}'):
        os.mkdir(f'{csv_files_path}/{date}')
        for actuator in actuators:
            with open(f'{csv_files_path}/{date}/{actuator}', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(actuator_attributes_csv_write)
                for row in actuator_dict[actuator].values():
                    csv_writer.writerow(row)
    else:
        pass

    actuator_dict.clear()
