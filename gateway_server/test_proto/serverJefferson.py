from flask import Flask, request
from flask_socketio import SocketIO


class WebSocketApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret'
        self.app.config['SESSION_TYPE'] = 'filesystem'
        self.socketio = SocketIO(self.app, cors_allowed_origins='*', async_mode=None)

        # Register routes
        self.register_routes()

        # Set up WebSocket event handlers
        self.set_up_socket_events()

    def register_routes(self):
        self.app.add_url_rule('/sign_up_user', 'sign_up_user', self.sign_up_user, methods=['POST'])
        self.app.add_url_rule('/login', 'login', self.get_user, methods=['POST'])

    def set_up_socket_events(self):
        self.socketio.on_event('get_tasks', self.get_tasks, namespace='/tasks')
        self.socketio.on_event('add_task', self.add_task, namespace='/tasks')

    def sign_up_user(self):
        # Get user data from the request
        message = request.data
        return {'user': message}

    def get_user(self):
        message = request.data
        return {'user': message}

    def add_task(self, message):
        print(message)
        # Return a response to the Flutter application
        self.socketio.emit('add_task', True)

    def get_tasks(self, message):
        id = message
        id = int(id)
        self.socketio.emit('add_task', True)

    def run(self):
        self.socketio.run(self.app, debug=True, host='127.0.0.1', port=5001)


if __name__ == '__main__':
    app = WebSocketApp()
    app.run()
