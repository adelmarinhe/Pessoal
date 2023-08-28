from threading import Lock


class RobotExecutionContext:
    """
    This class is responsible for storing the all robot execution context. This class works as a singleton.
    The singleton instance is created at the end of the module.
    """
    def __init__(self) -> None:
        self.__execution_status = ''
        self.__connected = False
        self.__paused = False
        self.__mutex = Lock()

    def get_execution_status(self):
        with self.__mutex:
            element = self.__execution_status
            return element

    def set_execution_status(self, execution_status):
        with self.__mutex:
            self.__execution_status = execution_status

    def is_connected(self):
        with self.__mutex:
            element = self.__connected
            return element

    def set_connected(self, connected):
        with self.__mutex:
            self.__connected = connected

    def is_paused(self):
        with self.__mutex:
            element = self.__paused
            return element

    def set_pause(self, pause):
        with self.__mutex:
            self.__paused = pause


robotContext = RobotExecutionContext()