from time import sleep
from back_end.controller.robot_provider.robot_execution_context import RobotContext, ExecutionStatus, ActionCommand, MoveType, RobotActuatorCommand
from concurrent.futures import ThreadPoolExecutor
# from rria_api.robot_facade import RobotObject
from pyniryo2 import NiryoRobot
from typing import Callable, Optional
from threading import Lock
import sys


class RobotProvider:
    __robot: Optional[NiryoRobot]

    def __init__(self):
        self.__thread_pool = ThreadPoolExecutor(max_workers=1)
        self.__robot_mutex = Lock()
        self.__update_function = None

    def robot(self):
        with self.__robot_mutex:
            element = self.__robot
            return element

    def connect_robot(self):
        if RobotContext.get_execution_status() != ExecutionStatus.RUNNING:
            _ = self.__thread_pool.submit(self.__connect_robot)
        else:
            print('robot running commands, stop to change connect')

    def attach_update_function(self, update_function: Callable):
        self.__update_function = update_function

    def __connect_robot(self):
        try:
            print('try connect')
            RobotContext.set_connected(True)
            self.__robot = NiryoRobot('169.254.200.200')
            self.__robot.tool.release_with_tool()
            self.__robot.arm.move_to_home_pose()
        except Exception as e:
            print(e)
            RobotContext.set_connected(False)

        sys.exit()

    def disconnect_robot(self):
        if RobotContext.get_execution_status() != ExecutionStatus.RUNNING:
            _ = self.__thread_pool.submit(self.__disconnect_robot)
        else:
            print('robot running commands, stop to change connect')

    def __disconnect_robot(self):
        try:
            print('try disconnect')
            RobotContext.set_execution_status(ExecutionStatus.STOPPED)
            RobotContext.clean_commands()
            self.__robot.arm.move_to_home_pose()
            self.__robot = None
            RobotContext.set_connected(False)
            RobotContext.set_execution_status(ExecutionStatus.IDLE)
        except Exception as e:
            print(e)

        sys.exit()

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
                    self.__robot.arm.move_to_home_pose()  # to home
                    RobotContext.clean_commands()
                    break
                elif action_command == ActionCommand.FLUSH_ERROR:
                    pass
                else:
                    print('action not supported on execution loop', action_command)

            command = RobotContext.dequeue_command()

            if command is None:
                RobotContext.set_execution_status(ExecutionStatus.IDLE)
                break

            RobotContext.set_execution_status(ExecutionStatus.RUNNING)
            print(command)
            if command == RobotActuatorCommand.GRASP:
                self.__robot.tool.grasp_with_tool()
            elif command == RobotActuatorCommand.RELEASE:
                self.__robot.tool.release_with_tool()
            elif command.type == MoveType.JOINT:
                self.__robot.arm.move_joints([command.joint1, command.joint2, command.joint3, command.joint4,
                                             command.joint5, command.joint6])
            elif command.type == MoveType.CARTESIAN:
                self.__robot.arm.move_pose([command.x, command.y, command.z, command.rx, command.ry, command.rz])

            if not RobotContext.has_commands() and RobotContext.get_execution_status() == ExecutionStatus.RUNNING:
                sleep(10)
                self.__update_function()

        sys.exit()
