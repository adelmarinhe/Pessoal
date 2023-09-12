from threading import Event
from flask import Flask, request, Response
from flask_socketio import SocketIO
from robot_execution_context import robotContext

from robot_move_service import RobotMoveService
from robot_stop_service import RobotStopService


class WebSocketApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret'
        self.app.config['SESSION_TYPE'] = 'filesystem'
        self.socketio = SocketIO(self.app, cors_allowed_origins='*', async_mode=None)
        self.__thread_robot_move = None
        self.__thread_robot_stop = None

        # Register routes
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/robot-api/ticket', 'start_dispense', self.start_dispense, methods=['POST'])
        self.app.add_url_rule('/robot-api/pause', 'pause', self.pause, methods=['POST'])
        self.app.add_url_rule('/robot-api/resume', 'resume', self.resume, methods=['POST'])
        self.app.add_url_rule('/robot-api/execution-status', 'execution-status', self.execution_status, methods=['GET'])
        self.app.add_url_rule('/robot-api/emergency-stop', 'emergency_stop', self.emergency_stop, methods=['POST'])

    def start_dispense(self):
        # Get user data from the request
        message = request.data
        print('remedio dispense')
        self.__thread_robot_move = RobotMoveService('dispensador')
        self.__thread_robot_move.daemon = True
        self.__thread_robot_move.start()

        return Response(status=200)

    def pause(self):
        # message = request.data
        print('set pause')
        print('obj', robotContext)
        robotContext.set_pause(True)

        return Response(status=200)

    def resume(self):
        # message = request.data
        print('obj', robotContext)
        print('set resume')
        robotContext.set_pause(False)
        return Response(status=200)

    def execution_status(self):
        # message = request.data
        print('set execution status')
        status = str(robotContext.get_execution_status())
        return Response(response=status, status=200)

    def emergency_stop(self):
        # message = request.data
        print('emergency stop')
        self.__thread_robot_stop = RobotStopService('emergency stop')
        self.__thread_robot_stop.daemon = True
        self.__thread_robot_stop.start()
        return Response(status=200)

    def run(self):
        self.socketio.run(self.app, debug=True, host='127.0.0.1', port=5001)


if __name__ == '__main__':
    app = WebSocketApp()
    app.run()
