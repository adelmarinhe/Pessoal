from time import sleep
from threading import Thread
from rria_api.robot_object import *
from robot_execution_context import robotContext
from robot_joint_command import RobotJointCommand


class RobotMoveService(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.__robot = None
        self.__moveList = [RobotJointCommand(0, 0, 40, 0, 0, 0), RobotJointCommand(0, 0, -40, 0, 0, 0), RobotJointCommand(0, 0, 0, 0, 0, 0), RobotJointCommand(30, 0, 40, 0, 0, 0)]
        self.__idx = 0

    def run(self):
        try:
            self.__robot = RobotObject('192.168.2.10', 'gen3')
            self.__robot.connect_robot()
        except Exception as e:
            return
        
        while True:
            if robotContext.is_paused():
                sleep(0.016)
                print('paused')
            else:
                print('running')
                robotContext.set_execution_status('robot move element ' + str(self.__idx))
                command = self.__moveList[self.__idx]
                try:
                    self.__robot.move_joints(command.joint_1, command.joint_2, command.joint_3, command.joint_4,
                                             command.joint_5, command.joint_6)
                    
                except  Exception as e:
                    print('force exit by exception')
                    self.__robot.disconnect_robot()
                    break
                self.__idx = (self.__idx + 1)%len(self.__moveList)