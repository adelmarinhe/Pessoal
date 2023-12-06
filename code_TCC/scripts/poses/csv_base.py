import json
from code_TCC.scripts.utils import actuator_utils as utils

json_files_path = utils.JSON_FILES_FOLDER_PATH
csv_files_path = utils.CSV_FILES_FOLDER

positions = utils.sequence

attributes = ["commandedToolPoseX", "commandedToolPoseY", "commandedToolPoseZ",
              "commandedToolPoseThetaX", "commandedToolPoseThetaY", "commandedToolPoseThetaZ"]

actuator_dict = {}
count = 0
data = [['position', 'commandedToolPoseX', 'commandedToolPoseY', 'commandedToolPoseZ',
         "commandedToolPoseThetaX", "commandedToolPoseThetaY", "commandedToolPoseThetaZ"]]

with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/json_data_files/2023-09-18.json', 'r') as json_file:
    json_data = json.load(json_file)

    date = '2023-09-18.json'.split(".")[0]

    instances = list(json_data.keys())

    for count, instance in enumerate(instances):
        position = json_data[instance][0]

        print(position)

        if position == 'Home' and count % 7 == 6:
            position = f"position_6"
        elif position == 'movement_2_safe_grasp':
            if count % 7 == 0:
                position = f"position_7"
            elif count % 7 == 2:
                position = f"position_2"
        elif position == 'movement_3_grasp' and count % 7 == 1:
            position = f"position_1"
        elif position == 'movement_4_safe_release':
            if count % 7 == 3:
                position = f"position_3"
            elif count % 7 == 5:
                position = f"position_5"
        elif position == 'movement_5_release' and count % 7 == 4:
            position = f"position_4"

        feedback_robot = json_data[instance][1]

        parsed_data = json.loads(feedback_robot)

        base_data = parsed_data['base']

        data_to_csv = [position, base_data['commandedToolPoseX'],
                       base_data['commandedToolPoseY'], base_data['commandedToolPoseZ'],
                       base_data['commandedToolPoseThetaX'], base_data['commandedToolPoseThetaY'],
                       base_data['commandedToolPoseThetaZ']]

        data.append(data_to_csv)

    print(data)

    # with open(f'C:/Users/jams/Documents/Pessoal/code_TCC/analyses/poses/{date}.csv', 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow(actuator_attributes_csv_write)
    #     for row in actuator_dict[actuator].values():
    #         csv_writer.writerow(row)
