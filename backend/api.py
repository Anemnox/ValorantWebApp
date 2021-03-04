import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

def main():
    """
    Starts up the messaging server at the given ip and port
    """
    app.run()


if __name__ == "__main__":
    main()