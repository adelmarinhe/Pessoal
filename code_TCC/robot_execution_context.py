import json

import utilities
from dataclasses import dataclass
from collections import deque
from enum import Enum, auto
from threading import Lock


class ExecutionStatus(Enum):
    RUNNING = auto()
    IDLE = auto()
    PAUSED = auto()
    STOPPED = auto()
    ERROR = auto()


class MoveType(Enum):
    JOINT = auto()
    CARTESIAN = auto()


class RobotType(Enum):
    KINOVA = auto()


class KinovaPositions:
    actions: dict = {}

    def __new__(cls, base=None):
        if base:
            cls.actions = utilities.get_actions_dict(base)
        return cls.actions


@dataclass
class RobotJointCommand:
    joint1: float = 0
    joint2: float = 0
    joint3: float = 0
    joint4: float = 0
    joint5: float = 0
    joint6: float = 0
    type: MoveType = MoveType.JOINT


@dataclass
class RobotCartesianCommand:
    x: float = 0
    y: float = 0
    z: float = 0
    rx: float = 0
    ry: float = 0
    rz: float = 0
    type: MoveType = MoveType.CARTESIAN


class RobotActuatorCommand(Enum):
    GRASP = auto()
    RELEASE = auto()


class RobotExecutionContext:
    def __init__(self) -> None:
        self.__command_queue = deque()
        self.__execution_status = ExecutionStatus.IDLE
        self.__conected = False
        self.__action_command = None
        self.__mutex = Lock()

    def enqueue_command(self, command) -> None:
        with self.__mutex:
            try:
                self.__command_queue += command
            except TypeError:
                self.__command_queue.append(command)

    def dequeue_command(self):
        with self.__mutex:
            if len(self.__command_queue) > 0:
                element = self.__command_queue.popleft()
                return element

    def check_for_commands(self):
        return len(self.__command_queue)

    def clean_commands(self):
        with self.__mutex:
            self.__command_queue.clear()

    def get_reset_action_command(self):
        with self.__mutex:
            element = self.__action_command
            self.__action_command = None
            return element

    def get_action_command(self):
        with self.__mutex:
            element = self.__action_command
            return element

    def set_action_command(self, action_command: ActionCommand):
        with self.__mutex:
            self.__action_command = action_command

    def reset_action_command(self):
        with self.__mutex:
            self.__action_command = None


RobotContext = RobotExecutionContext()
