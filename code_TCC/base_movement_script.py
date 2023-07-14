#! /usr/bin/env python3
import os
import json
import random
import utilities
import threading
from pathlib import Path
from datetime import datetime
# from emergency_stop import EmergencyStop
from kortex_api.autogen.messages import Base_pb2
from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient


FILES_FOLDER = "json_data_files"


def get_actions_dict(base):
    """
    Get the list of available actions from the Kinova database
    """

    action_dict = {}
    action_types = [Base_pb2.REACH_JOINT_ANGLES, Base_pb2.END_EFFECTOR_TYPE_UNSPECIFIED]
    for at in action_types:
        action_type = Base_pb2.RequestedActionType()
        action_type.action_type = at
        action_list = base.ReadAllActions(action_type)
        action_dict.update({action.name: action for action in action_list.action_list})
    return action_dict


def movement_sequence(base):
    """
    Example of a sequence of movements
    """

    print("Creating Action for Sequence")
    action_dict = get_actions_dict(base)

    print("Creating Sequence")
    sequence = Base_pb2.Sequence()
    sequence.name = "Example sequence"

    sequences = {'Sequence 1': ['Time4_safe_remedio1', 'Time4_abrir_garra_remedio', 'Time4_remedio1',
                                'Time4_fechar_garra_remedio', 'Time4_safe_remedio1', 'Time4_soltar_remedio',
                                'Time4_caixinha', 'Time4_abrir_garra_remedio', 'Time4_fechar_garra_remedio',
                                'Home'],
                 'Sequence 2': ['Time4_safe_remedio2', 'Time4_abrir_garra_remedio', 'Time4_remedio2',
                                'Time4_fechar_garra_remedio', 'Time4_safe_remedio2', 'Time4_soltar_remedio',
                                'Time4_caixinha', 'Time4_abrir_garra_remedio', 'Time4_fechar_garra_remedio',
                                'Home'],
                 'Sequence 3': ['Time4_safe_remedio3', 'Time4_abrir_garra_remedio', 'Time4_remedio3',
                                'Time4_fechar_garra_remedio', 'Time4_safe_remedio3', 'Time4_soltar_remedio',
                                'Time4_caixinha', 'Time4_abrir_garra_remedio', 'Time4_fechar_garra_remedio',
                                'Home'],
                 'Sequence 4': ['Time4_safe_remedio4', 'Time4_abrir_garra_remedio', 'Time4_remedio4',
                                'Time4_fechar_garra_remedio', 'Time4_safe_remedio4', 'Time4_soltar_remedio',
                                'Time4_caixinha', 'Time4_abrir_garra_remedio', 'Time4_fechar_garra_remedio',
                                'Home']
                 }

    random_mode = False

    if random_mode:
        executed_sequence = random.choice(list(sequences.keys()))
    else:
        executed_sequence = 'Sequence 1'

    print("Appending Actions to Sequence")
    for i, task_name in enumerate(sequences[executed_sequence]):
        task = sequence.tasks.add()
        task.group_identifier = i
        task.action.CopyFrom(action_dict[task_name])

    e = threading.Event()
    notification_handle = base.OnNotificationSequenceInfoTopic(
        utilities.check_for_sequence_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Creating sequence on device and executing it")
    handle_sequence = base.CreateSequence(sequence)
    base.PlaySequence(handle_sequence)

    print("Waiting for movement to finish ...")
    finished = e.wait(utilities.TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    if not finished:
        print("Timeout on action notification wait")
    return finished


def data_cyclic(base_cyclic, data):
    """
    Example of a cyclic data acquisition
    """

    feedback = base_cyclic.RefreshFeedback()
    current_timestamp = datetime.now().strftime("%H:%M:%S")

    data[current_timestamp] = [f'{feedback}']

    return data


def save_data(data):
    """
    Save data in a json file
    """
    with open(f"{FILES_FOLDER}/{file_name()}", 'w') as output:
        json.dump(data, output)


def create_file(name):
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
    current_date = date.strftime("%Y-%m-%d")
    return f'{current_date}.json'


def main():
    """
    Example of a pick and place scenario with the Kortex API
    """

    # Parse arguments
    args = utilities.parseConnectionArguments()

    number_of_cycles = 30

    data = create_file(file_name())

    # Create connection to the device and get the router
    with utilities.DeviceConnection.createTcpConnection(args) as router:
        # Create required services
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)

        # EmergencyStop(router).emergency_stop()

        success = True
        for repetitions in range(number_of_cycles):
            success &= movement_sequence(base)
            save_data(data_cyclic(base_cyclic, data))

        return 0 if success else 1


if __name__ == "__main__":
    exit(main())
