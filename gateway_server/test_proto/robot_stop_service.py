from threading import Thread
from rria_api.robot_object import *


class RobotStopService(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.__robot = None
        
    def run(self):
        print('start connect to robot RobotStopService')

        self.__robot = RobotObject('192.168.2.10', 'gen3')
        self.__robot.connect_robot()
        self.__robot.apply_emergency_stop()
