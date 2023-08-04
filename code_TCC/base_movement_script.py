#! /usr/bin/env python3
import os
import json
import random
import utilities
import threading
from datetime import datetime
from emergency_stop import EmergencyStop
from kortex_api.autogen.messages import Base_pb2
from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient


FILES_FOLDER = "json_data_files"

sequences = {}
for i in range(1, 4):
    sequences[f'Sequence {i}'] = [f'Time4_safe_remedio{i}', 'Time4_abrir_garra_remedio', f'Time4_remedio{i}',
                                 'Time4_fechar_garra_remedio', f'Time4_safe_remedio{i}', 'Time4_soltar_remedio',
                                 'Time4_caixinha', 'Time4_abrir_garra_remedio', 'Time4_fechar_garra_remedio', 'Home']


def movement_action(base, action_name):
    """
    Example of a movement action
    """

    base_servo_mode = Base_pb2.ServoingModeInformation()
    base_servo_mode.servoing_mode = Base_pb2.SINGLE_LEVEL_SERVOING
    base.SetServoingMode(base_servo_mode)

    action_handle_dict = utilities.get_actions_handle_dict(base)
    action_handle = None

    if action_name in action_handle_dict:
        action_handle = action_handle_dict[action_name]

    if action_handle is None:
        print("Can't reach safe position. Exiting")
        return False

    return utilities.execute_action(action_handle, base)


def obtain_feedback(base_cyclic):
    """
    Obtain feedback
    """

    feedback = base_cyclic.RefreshFeedback()

    return feedback


def data_cyclic(base_cyclic, data, movement: None):
    """
    Example of a cyclic data acquisition
    """

    current_timestamp = datetime.now().strftime("%H:%M:%S")

    data[current_timestamp] = [f'{movement}', f'{obtain_feedback(base_cyclic)}']

    return data


def check_faults(base, base_cyclic):
    """
    Check if there are any faults
    """

    if "fault" in f'{obtain_feedback(base_cyclic)}':
        clear_faults(base)


def clear_faults(base):
    """
    Clear the faults of the robot
    """

    base.ClearFaults()


def save_data(data):
    """
    Save data in a json file
    """

    with open(f"{FILES_FOLDER}/{file_name()}", 'w') as output:
        json.dump(data, output)


def create_file(name):
    """
    Create a json file with the data
    """

    if not os.path.isdir(FILES_FOLDER):
        os.mkdir(FILES_FOLDER)

    if os.path.isfile(f"{FILES_FOLDER}/{name}"):
        # open json file
        with open(f"{FILES_FOLDER}/{name}", 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {}

    return data


def file_name(date=datetime.now()):
    """
    Create a file name with the current date
    """

    current_date = date.strftime("%Y-%m-%d")

    return f'{current_date}.json'


def main():
    """
    Example of a pick and place scenario with the Kortex API
    """

    args = utilities.parse_connection_arguments()

    number_of_cycles = 90

    data = create_file(file_name())

    # Create connection to the device and get the router
    with utilities.DeviceConnection.create_tcp_connection(args) as router:
        # Create required services
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)
        success = True

        for repetitions in range(number_of_cycles):
            for movement in sequences['Sequence 1']:
                save_data(data_cyclic(base_cyclic, data, movement))
                check_faults(base, base_cyclic)
                success &= movement_action(movement, base)

        return 0 if success else 1


if __name__ == "__main__":
    exit(main())