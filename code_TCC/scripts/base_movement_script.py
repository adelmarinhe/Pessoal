import os
import json
import kinova_utilities
import threading
from datetime import datetime
from google.protobuf import json_format

from code_TCC.scripts import utils
from emergency_stop import EmergencyStop
from kortex_api.autogen.messages import Base_pb2
from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient

json_files_path = utils.JSON_FILES_FOLDER_PATH

sequence = utils.sequence


def get_actions_handle_dict(base):
    """
    Get the list of available actions from the Kinova database
    """

    action_handle_dict = {}
    action_types = [Base_pb2.REACH_JOINT_ANGLES, Base_pb2.END_EFFECTOR_TYPE_UNSPECIFIED]
    for at in action_types:
        action_type = Base_pb2.RequestedActionType()
        action_type.action_type = at
        action_list = base.ReadAllActions(action_type)
        action_handle_dict.update({action.name: action.handle for action in action_list.action_list})

    return action_handle_dict


def wait_execution(base, event, notification_handle):
    """
    Wait for the current action to finish execution
    """

    print("Waiting execution")
    finished = event.wait(kinova_utilities.TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    if finished:
        print("Movement completed")
    else:
        print("Timeout on action notification wait")

    return finished


def movement_action(base, action_name):
    """
    Example of a movement action
    """

    base_servo_mode = Base_pb2.ServoingModeInformation()
    base_servo_mode.servoing_mode = Base_pb2.SINGLE_LEVEL_SERVOING
    base.SetServoingMode(base_servo_mode)

    action_handle_dict = get_actions_handle_dict(base)
    action_handle = None

    if action_name in action_handle_dict:
        action_handle = action_handle_dict[action_name]

    if action_handle is None:
        print("Can't reach safe position. Exiting")
        return False

    thread_event = threading.Event()
    notification_handle = base.OnNotificationSequenceInfoTopic(
        kinova_utilities.check_for_end_or_abort(thread_event),
        Base_pb2.NotificationOptions()
    )

    return kinova_utilities.execute_action(action_handle, base)


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


def data_cyclic_json(base_cyclic, feedback_json, movement):
    current_timestamp = datetime.now().strftime("%H:%M:%S")

    feedback_json[current_timestamp] = [f'{movement}', json_format.MessageToJson(obtain_feedback(base_cyclic))]

    return feedback_json


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

    with open(f"{json_files_path}/{file_name()}", 'w') as output:
        json.dump(data, output)


def create_file(name):
    """
    Create a json file with the data
    """

    if not os.path.isdir(json_files_path):
        os.mkdir(json_files_path)

    if os.path.isfile(f"{json_files_path}/{name}"):
        # open json file
        with open(f"{json_files_path}/{name}", 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {}

    return data


def get_time(time=datetime.now()):
    """
    Get the current time
    """

    return time.strftime("%H:%M:%S")


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

    args = kinova_utilities.parse_connection_arguments()

    time_goal = datetime(2023, 9, 30, 17, 10)

    data = create_file(file_name())

    # Create connection to the device and get the router
    with kinova_utilities.DeviceConnection.create_tcp_connection(args) as router:
        # Create required services
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)
        success = True

        while datetime.now() < time_goal:
            for movement in sequence:
                save_data(data_cyclic_json(base_cyclic, data, movement))
                check_faults(base, base_cyclic)
                success &= movement_action(base, movement)

        print(datetime.now())

        return 0 if success else 1


if __name__ == "__main__":
    exit(main())
