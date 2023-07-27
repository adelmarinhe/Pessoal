import pandas as pd
import json
import os

base_attributes = ['active_state_connection_identifier', 'active_state', 'arm_voltage', 'temperature_cpu',
                   'imu_acceleration_x', 'imu_acceleration_y', 'imu_acceleration_z', 'imu_angular_velocity_x',
                   'imu_angular_velocity_y', 'imu_angular_velocity_z', 'tool_pose_x', 'tool_pose_y', 'tool_pose_z',
                   'tool_pose_theta_x', 'tool_pose_theta_y', 'tool_pose_theta_z', 'tool_twist_linear_x',
                   'tool_twist_linear_y', 'tool_twist_linear_z', 'tool_twist_angular_x', 'tool_twist_angular_y',
                   'tool_twist_angular_z', 'tool_external_wrench_force_x', 'tool_external_wrench_force_y',
                   'tool_external_wrench_force_z', 'tool_external_wrench_torque_x', 'tool_external_wrench_torque_y',
                   'tool_external_wrench_torque_z', 'fault_bank_a', 'fault_bank_b', 'warning_bank_a', 'warning_bank_b',
                   'commanded_tool_pose_x', 'commanded_tool_pose_y', 'commanded_tool_pose_z',
                   'commanded_tool_pose_theta_x', 'commanded_tool_pose_theta_y', 'commanded_tool_pose_theta_z']
actuator_attributes = ['command_id', 'status_flags', 'jitter_comm', 'position', 'velocity', 'torque', 'current_motor',
                       'voltage', 'temperature_motor', 'temperature_core', 'fault_bank_a', 'fault_bank_b',
                       'warning_bank_a', 'warning_bank_b']
interconnect_attributes = ['identifier', 'status_flags', 'jitter_comm', 'voltage', 'temperature_core']
gripper_attributes = ['motor_id', 'position', 'velocity', 'current_motor', 'temperature_motor']

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"


def find_string(start_string: str, end_string: str, data: dict, instance, addition_term=0):
    """
    Method to find string in json
    """

    start_index = data[instance].find(start_string) + len(start_string) + addition_term
    end_index = data[instance].find(end_string, start_index)
    string_data = data[instance][start_index:end_index]

    return string_data


def parse_base(data: dict):
    """
    Method to return a dictionary of the base data
    """

    base_dict = {}
    base_attributes_return = {}

    for instance in data.keys():
        base_data = find_string("base {\n  ", "\n}", data, instance)

        base_dict[instance] = {}

        lines = base_data.split("\n  ")

        for line in lines:
            key, value = line.split(': ')
            base_dict[instance][key.strip()] = value.strip()

        base_attributes_return[instance] = []

        for attribute in base_attributes:
            list_item = base_dict[instance][attribute] if attribute in list(base_dict[instance].keys()) else " "
            base_attributes_return[instance].append(list_item)

    return base_attributes_return


def parse_actuators(data: dict):
    """
    Method to return a list of dictionaries of the actuators data
    """

    actuators = [f'Actuator {i + 1}' for i in range(6)]
    actuators_data = {}
    actuator_dict = {}
    actuator_attributes_return = {}

    for instance in data.keys():
        actuators_data[instance] = {}
        actuator_dict[instance] = {}
        actuator_attributes_return[instance] = {}
        for actuator in actuators:
            actuators_data[instance][actuator] = []
            start_index = 0 if 'Actuator 1' else data[instance].find("actuators {") + len("actuators {")
            actuators_data[instance][actuator] = find_string("actuators {\n ", "\n}", data, instance,
                                                             actuators.index(actuator) * start_index)

            actuator_dict[instance][actuator] = {}
            lines = actuators_data[instance][actuator].split('\n ')
            for line in lines:
                key, value = line.split(':')
                actuator_dict[instance][actuator][key.strip()] = value.strip()

            actuator_attributes_return[instance][actuator] = []
            for attribute in actuator_attributes:
                list_item = actuator_dict[instance][actuator][attribute] if attribute in list(
                    actuator_dict[instance][actuator].keys()) else " "
                actuator_attributes_return[instance][actuator].append(list_item)

    return actuator_attributes_return


def parse_interconnect(data: dict):
    """
    Method to return a list of dictionaries of the interconnect data
    """

    interconnect_dict = {}
    interconnect_attributes_return = {}

    for instance in data.keys():
        interconnect_dict[instance] = {}
        interconnect_attributes_return[instance] = []

        feedback_id = find_string("feedback_id {\n", "\n  }", data, instance)
        interconnect_data = find_string("\n  }\n", "\n  gripper", data, instance)

        lines = [feedback_id]
        for parameter in interconnect_data.split("\n"):
            lines.append(parameter)

        for line in lines:
            key, value = line.split(':')
            interconnect_dict[instance][key.strip()] = value.strip()

        for attribute in interconnect_attributes:
            list_item = interconnect_dict[instance][attribute] if attribute in list(
                interconnect_dict[instance].keys()) else " "
            interconnect_attributes_return[instance].append(list_item)

    return interconnect_attributes_return


def parse_gripper(data: dict):
    """
    Method to return a list of dictionaries of the interconnect data
    """
    gripper_dict = {}
    gripper_attributes_return = {}

    for instance in data.keys():
        gripper_dict[instance] = {}
        gripper_attributes_return[instance] = []

        motor_data = find_string("motor {\n", "\n    }", data, instance)

        lines = []

        for parameter in motor_data.split("\n"):
            lines.append(parameter)

        for line in lines:
            key, value = line.split(':')
            gripper_dict[instance][key.strip()] = value.strip()

        for attribute in gripper_attributes:
            list_item = gripper_dict[instance][attribute] if attribute in list(gripper_dict[instance].keys()) else " "
            gripper_attributes_return[instance].append(list_item)

    return gripper_attributes_return


for file in os.listdir(JSON_FILES_FOLDER):
    with open(f'{JSON_FILES_FOLDER}/{file}', 'r') as json_file:
        json_data = json.load(json_file)

base_data_dict = parse_base(json_data)
actuators_data_dict = parse_actuators(json_data)
interconnect_data_dict = parse_interconnect(json_data)
motor_data_dict = parse_gripper(json_data)

# Print the combined dictionary
print(actuators_data_dict)
print(base_data_dict)
print(interconnect_data_dict)
print(motor_data_dict)
