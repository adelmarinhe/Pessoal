import pandas as pd
import json
import os

# base_attributes = [active_state_connection_identifier, active_state, arm_voltage, temperature_cpu, imu_acceleration_x, imu_acceleration_y, imu_acceleration_z, imu_angular_velocity_x, imu_angular_velocity_y, imu_angular_velocity_z, tool_pose_x, tool_pose_y, tool_pose_z, tool_pose_theta_x, tool_pose_theta_y, tool_pose_theta_z, tool_twist_linear_x, tool_twist_linear_y, tool_twist_linear_z, tool_twist_angular_x, tool_twist_angular_y, tool_twist_angular_z, tool_external_wrench_force_x, tool_external_wrench_force_y, tool_external_wrench_force_z, tool_external_wrench_torque_x, tool_external_wrench_torque_y, tool_external_wrench_torque_z, commanded_tool_pose_x, commanded_tool_pose_y, commanded_tool_pose_z, commanded_tool_pose_theta_x, commanded_tool_pose_theta_y, commanded_tool_pose_theta_z]
# actuator_attributes = [command_id, status_flags, jitter_comm, position, velocity, torque, current_motor, voltage, temperature_motor, temperature_core]
# interconnect_attributes = [feedback_id, status_flags, jitter_comm, voltage, temperature_core, gripper_feedback]
# motor_attibutes = [motor_id, position, velocity, current_motor, temperature_motor]
# gripper_attributes = []

# json_string = "base {\n  active_state_connection_identifier: 28524\n  active_state: ARMSTATE_IN_FAULT\n  arm_voltage: 24.066713333129883\n  temperature_cpu: 57.06097412109375\n  imu_acceleration_x: -0.12914331257343292\n  imu_acceleration_y: 9.710067749023438\n  imu_acceleration_z: 0.08287568390369415\n  imu_angular_velocity_x: 4.1126275062561035\n  imu_angular_velocity_y: -0.7582118511199951\n  imu_angular_velocity_z: 0.8150253891944885\n  tool_pose_x: 0.0654463842511177\n  tool_pose_y: -0.011876634322106838\n  tool_pose_z: 1.0029680728912354\n  tool_pose_theta_x: 0.19145791232585907\n  tool_pose_theta_y: -0.010648015886545181\n  tool_pose_theta_z: 90.02140045166016\n  tool_twist_linear_x: 4.22011835325975e-05\n  tool_twist_linear_y: 3.181410284014419e-05\n  tool_twist_linear_z: -4.700296358350897e-06\n  tool_twist_angular_x: -0.006283061113208532\n  tool_twist_angular_y: 0.004732893314212561\n  tool_twist_angular_z: 0.005624959245324135\n  tool_external_wrench_force_x: -0.43804991245269775\n  tool_external_wrench_force_y: 0.07263864576816559\n  tool_external_wrench_force_z: 0.010520769283175468\n  tool_external_wrench_torque_x: 0.0005708439275622368\n  tool_external_wrench_torque_y: 0.01721472479403019\n  tool_external_wrench_torque_z: 0.11520756781101227\n  fault_bank_a: 8388608\n  commanded_tool_pose_x: 0.06530550122261047\n  commanded_tool_pose_y: -0.011916915886104107\n  commanded_tool_pose_z: 1.0029833316802979\n  commanded_tool_pose_theta_x: 0.1768769472837448\n  commanded_tool_pose_theta_y: -0.016513381153345108\n  commanded_tool_pose_theta_z: 90.00238037109375\n}\nactuators {\n  command_id: 2147520830\n  status_flags: 33590288\n  jitter_comm: 116347540\n  position: 359.0545349121094\n  velocity: -0.0013630680041387677\n  torque: 0.21993939578533173\n  current_motor: -0.1849592626094818\n  voltage: 23.90185546875\n  temperature_motor: 27.928850173950195\n  temperature_core: 42.20883560180664\n}\nactuators {\n  command_id: 2147586366\n  status_flags: 33590288\n  jitter_comm: 116347003\n  position: 358.560791015625\n  velocity: -0.0003027327184099704\n  torque: -0.5267891883850098\n  current_motor: 0.1323590874671936\n  voltage: 23.804296493530273\n  temperature_motor: 28.802608489990234\n  temperature_core: 39.44881820678711\n}\nactuators {\n  command_id: 2147651902\n  status_flags: 33590288\n  jitter_comm: 116346991\n  position: 358.7523193359375\n  velocity: -0.0027245674282312393\n  torque: 0.3848939538002014\n  current_motor: -0.3223170042037964\n  voltage: 23.796167373657227\n  temperature_motor: 29.45681381225586\n  temperature_core: 42.11155319213867\n}\nactuators {\n  command_id: 2147717438\n  status_flags: 33590288\n  jitter_comm: 116348203\n  position: 359.23199462890625\n  velocity: 0.00849564652889967\n  torque: 0.10982371121644974\n  current_motor: -0.1899936944246292\n  voltage: 23.73112678527832\n  temperature_motor: 27.353126525878906\n  temperature_core: 42.74900436401367\n}\nactuators {\n  command_id: 2147782974\n  status_flags: 33590288\n  jitter_comm: 116347994\n  position: 0.00848388671875\n  velocity: 0.012729169800877571\n  torque: -0.07321580499410629\n  current_motor: 0.12712642550468445\n  voltage: 23.755517959594727\n  temperature_motor: 28.091676712036133\n  temperature_core: 42.42424392700195\n}\nactuators {\n  command_id: 2147914046\n  status_flags: 33590288\n  jitter_comm: 116346783\n  position: 1.7346343994140625\n  velocity: -0.008334575220942497\n  torque: 0.029951922595500946\n  current_motor: -0.0521114207804203\n  voltage: 23.8612060546875\n  temperature_motor: 27.376386642456055\n  temperature_core: 43.93939208984375\n}\ninterconnect {\n  feedback_id {\n    identifier: 2147847762\n  }\n  status_flags: 33557520\n  jitter_comm: 116328932\n  voltage: 23.6986083984375\n  temperature_core: 45.49407196044922\n  gripper_feedback {\n    motor {\n      motor_id: 1\n      position: 0.005812871735543013\n      current_motor: -0.006495471112430096\n      temperature_motor: 25.809152603149414\n    }\n  }\n}\n"

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"





def parse_base(data: dict):
    """
        Method to return a dictionary of the base data
        """

    base_dict = {}

    for instance in instances:
        start_index = data[instance].find("base {\n  ") + len("base {\n  ")
        end_index = data[instance].find("\n}", start_index)
        base_data = data[instance][start_index:end_index]

        base_dict[instance] = []

        lines = base_data.split("\n  ")
        for line in lines:
            key, value = line.split(': ')
            base_dict[instance].append(value.strip())

        return base_dict


def parse_actuators(data: dict):
    """
        Method to return a list of dictionaries of the actuators data
        """

    actuators = [f'Actuator {i + 1}' for i in range(6)]
    actuators_data = {}
    actuator_dict = {}

    for instance in instances:
        for actuator in actuators:
            actuators_data[instance] = {}
            actuators_data[instance][actuator] = []
            start_index = data[instance].find("actuators {") + len("actuators {")
            end_index = data[instance].find("\n}", start_index)
            actuators_data[instance][actuator] = data[instance][start_index:end_index].strip()

            actuator_dict[instance] = {}
            lines = actuators_data[instance][actuator].split('\n ')
            values = []
            for line in lines:
                key, value = line.split(':')
                values.append(value.strip())
            actuator_dict[instance][actuator] = values
            values.clear()


    #TODO: insert this dictionary into a pandas dataframe
    # return actuator_dict
    return actuators_data

# def parse_interconnect(data):
#     start_index = data.find("interconnect {")
#     end_index = data.find("}", start_index) + 1
#     interconnect_data = data[start_index:end_index]
#     interconnect_dict = {}
#     lines = interconnect_data.split("\n")
#     for line in lines:
#         if line.strip():
#             key, value = line.split(":")
#             interconnect_dict[key.strip()] = value.strip()
#     return interconnect_dict


for file in os.listdir(JSON_FILES_FOLDER):
    with open(f'{JSON_FILES_FOLDER}/{file}', 'r') as json_file:
        json_data = json.load(json_file)

instances = list(json_data.keys())

base_data_dict = parse_base(json_data)
actuators_data_dict = parse_actuators(json_data)
# interconnect_data_dict = parse_interconnect(json_string)


# combined_dict = {
#     "base": base_data_dict,
#     "actuators": actuators_data_dict,
#     "interconnect": interconnect_data_dict
# }

# Print the combined dictionary
print(actuators_data_dict)
print(base_data_dict)














