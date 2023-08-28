import json
import os
import csv

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"

data_classes = ['base', 'actuator_1', 'actuator_2', 'actuator_3', 'actuator_4', 'actuator_5', 'actuator_6', 'interconnect' ]


for file in os.listdir(JSON_FILES_FOLDER):
    with open(f'{JSON_FILES_FOLDER}/{file}', 'r') as json_file:
        json_data = json.load(json_file)

        instances = list(json_data.keys())
        for instance in instances:
            movement = json_data[instance][0]
            json_string = json_data[instance][1]

            parsed_data = json.loads(json_string)

            base_data = parsed_data['base']
            actuator_data = parsed_data['actuators']
            gripper_data = parsed_data['interconnect']

            # base_data_list = []
            actuator_data_dict = {}
            actuator_data_dict_2 = []
            # gripper_data_dict = [file, instance, movement]

            # base_data_2 = []

            # for attribute in list(base_data.keys()):
            #     base_data_2.append(base_data[attribute] if attribute in list(base_data.keys()) else " ")
            #     base_data_list.append(base_data_2)
            #     base_data_2.clear()

            for actuator in range(len(actuator_data)):
                for parameter in actuator_data[actuator]:
                    actuator_data_dict_2.append(actuator_data[actuator][parameter])
                actuator_data_dict[actuator] = actuator_data_dict_2

            # for attribute in gripper_data:
            #     gripper_data_dict.append(gripper_data[attribute] if attribute in list(gripper_data.keys()) else " ")

            # for data_class in actuators:
            #     with open(data_class, 'w', newline='') as csvfile:
            #         csv_writer = csv.writer(csvfile)
            #         for row in base_data_list:
            #             csv_writer.writerow(row)