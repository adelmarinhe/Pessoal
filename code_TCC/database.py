import pandas as pd
import json
import os

# base_attributes = [active_state_connection_identifier, active_state, arm_voltage, temperature_cpu, imu_acceleration_x, imu_acceleration_y, imu_acceleration_z, imu_angular_velocity_x, imu_angular_velocity_y, imu_angular_velocity_z, tool_pose_x, tool_pose_y, tool_pose_z, tool_pose_theta_x, tool_pose_theta_y, tool_pose_theta_z, tool_twist_linear_x, tool_twist_linear_y, tool_twist_linear_z, tool_twist_angular_x, tool_twist_angular_y, tool_twist_angular_z, tool_external_wrench_force_x, tool_external_wrench_force_y, tool_external_wrench_force_z, tool_external_wrench_torque_x, tool_external_wrench_torque_y, tool_external_wrench_torque_z, commanded_tool_pose_x, commanded_tool_pose_y, commanded_tool_pose_z, commanded_tool_pose_theta_x, commanded_tool_pose_theta_y, commanded_tool_pose_theta_z]
# actuator_attributes = [command_id, status_flags, jitter_comm, position, velocity, torque, current_motor, voltage, temperature_motor, temperature_core]
# interconnect_attributes = [feedback_id, status_flags, jitter_comm, voltage, temperature_core, gripper_feedback]
# motor_attibutes = [motor_id, position, velocity, current_motor, temperature_motor]
# gripper_attributes = []

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"

for file in os.listdir(JSON_FILES_FOLDER):
    with open(f'{JSON_FILES_FOLDER}/{file}', 'r') as json_file:
        data = json.load(json_file)

instances = list(data.keys())

# for instance in instances:
#     data_edit = data[instance].split('}')
#     # base_data = [base[]
#     print(data_edit)

data_edit = data[instances[3]].split(' ' and '\n')

print(data_edit)