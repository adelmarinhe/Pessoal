# from rria_api.robot_facade import RobotObject
from robot_execution_context import RobotContext, ExecutionStatus, ActionCommand, \
    MoveType, RobotActuatorCommand, \
    RobotType, KinovaPositions
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient
from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
import utilities
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Optional, Union
from threading import Lock
from time import sleep
import sys


class RobotProvider:
    __robot: Optional[Union[NiryoRobot, utilities.DeviceConnection]] = None

    def __init__(self, robot_type: RobotType):
        self.__thread_pool = ThreadPoolExecutor(max_workers=1)
        self.__robot_mutex = Lock()
        self.__update_function = None
        self.__robot_type = robot_type
        self.__kinova_args = {}  # Only used with Kinova

    @property
    def kinova_base(self):
        return self.__kinova_args.get("base")

    def robot(self):
        with self.__robot_mutex:
            element = self.__robot
            return element

    def attach_update_function(self, update_function: Callable):
        self.__update_function = update_function

    def emergency_stop(self):
        pass

    def safety_restart(self):
        pass

    def flush_robot_error(self):
        pass

    def run_commands(self):
        _ = self.__thread_pool.submit(self.__run_commands)

    def __run_commands(self):
        if not RobotContext.is_connected():
            print('robot connection not started')
            RobotContext.set_execution_status(ExecutionStatus.IDLE)
            return

        RobotContext.set_execution_status(ExecutionStatus.RUNNING)

        while True:
            action_command = RobotContext.get_reset_action_command()
            if action_command is not None:
                if action_command == ActionCommand.PAUSE:
                    print("PAUSED")
                    RobotContext.set_execution_status(ExecutionStatus.PAUSED)
                    break
                elif action_command == ActionCommand.STOP:
                    print("STOPPED")
                    RobotContext.set_execution_status(ExecutionStatus.STOPPED)
                    self.__kinova_command(KinovaPositions()['Zero'])
                    RobotContext.clean_commands()
                    break
                else:
                    print('action not supported on execution loop', action_command)

            command = RobotContext.dequeue_command()

            if command is None:
                RobotContext.set_execution_status(ExecutionStatus.IDLE)
                break

            RobotContext.set_execution_status(ExecutionStatus.RUNNING)

            if self.__robot_type == RobotType.KINOVA:
                self.__kinova_command(command)
            else:
                print("Unexpected robot type")

            if not RobotContext.check_for_commands() and RobotContext.get_execution_status() == ExecutionStatus.RUNNING:
                sleep(10)
                self.__update_function()

        sys.exit()

    def main(self):
        self.__kinova_command(KinovaPositions()[position])

    def __kinova_command(self, cmd):
        utilities.execute_action(cmd, self.kinova_base)
