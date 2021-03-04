from flask import Flask
from flask_socketio import SocketIO, send, emit

HOST_IP = "0.0.0.0"
HOST_PORT = "4000"

app = Flask(__name__)
sio = SocketIO(app, cors_allowed_origins="*")

@sio.on("connect")
def sendMessage():
    sio.emit("Message", "Server Connected!")


def main():
    """
    Starts up the messaging server at the given ip and port
    """
    sio.run(app, host=HOST_IP, port=HOST_PORT)


if __name__ == "__main__":
    main()
