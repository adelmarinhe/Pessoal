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


def execute_command(base, execution_action):
    """
    Check for messages from the robot
    """

    e = threading.Event()
    notification_handle = base.OnNotificationSequenceInfoTopic(
        utilities.check_for_sequence_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    if isinstance(execution_action, Base_pb2.Sequence):
        print("Creating sequence on device and executing it")
        handle = base.CreateSequence(execution_action)
        base.PlaySequence(handle)
    elif isinstance(execution_action, Base_pb2.Action):
        print("Creating movement action on device and executing it")
        handle = base.CreateAction(execution_action)
        base.ExecuteAction(handle)
    else:
        print("Type non supported")

    print("Waiting execution")
    finished = e.wait(utilities.TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    if finished:
        print("Movement completed")
    else:
        print("Timeout on action notification wait")
    return finished


def movement_sequence(base, seq):
    """
    Example of a sequence of movements
    """

    print("Creating Action for Sequence")
    action_dict = get_actions_dict(base)

    print("Creating Sequence")
    sequence = Base_pb2.Sequence()
    sequence.name = "Example sequence"

    random_mode = False

    if random_mode:
        executed_sequence = random.choice(list(seq.keys()))
    else:
        executed_sequence = 'Sequence 1'

    print("Appending Actions to Sequence")
    for i, task_name in enumerate(seq[executed_sequence]):
        task = sequence.tasks.add()
        task.group_identifier = i
        task.action.CopyFrom(action_dict[task_name])

    execute_command(base, sequence)

    return True if execute_command(base, sequence) else False


def movement_action(base, action_name):
    """
    Example of a movement action
    """

    print("Creating Action for Movement")
    action_dict = get_actions_dict(base)

    print("Creating Movement Action")
    movement_action = Base_pb2.Action()
    movement_action.name = action_name
    movement_action.application_data = "Movement Action"

    print("Appending Actions to Movement Action")
    # task = movement_action.tasks.add()
    # task.group_identifier = 0
    # task.action.CopyFrom(action_dict[action_name])

    execute_command(base, movement_action)


def data_cyclic(base_cyclic, data):
    """
    Example of a cyclic data acquisition
    """

    feedback = base_cyclic.RefreshFeedback()
    current_timestamp = datetime.now().strftime("%H:%M:%S")

    data[current_timestamp] = [f'{feedback}']

    return data


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

    # Parse arguments
    args = utilities.parseConnectionArguments()

    number_of_cycles = 2

    data = create_file(file_name())

    # Create connection to the device and get the router
    with utilities.DeviceConnection.createTcpConnection(args) as router:
        # Create required services
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)
        success = True

        EmergencyStop(base, data, data_cyclic, save_data, base_cyclic).emergency_stop()

        feedback = base_cyclic.RefreshFeedback()
        print(feedback)
        # robot executes movement action
        # for repetitions in range(number_of_cycles):
        #     for movement in sequences['Sequence 1']:
        #         clear_faults(base)
        #         success &= movement_action(base, movement)
        #         save_data(data_cyclic(base_cyclic, data))

        # robot executes movement sequence
        for repetitions in range(number_of_cycles):
            save_data(data_cyclic(base_cyclic, data))
            clear_faults(base)
            success &= movement_sequence(base, sequences)
            # save_data(data_cyclic(base_cyclic, data))

        return 0 if success else 1


if __name__ == "__main__":
    exit(main())