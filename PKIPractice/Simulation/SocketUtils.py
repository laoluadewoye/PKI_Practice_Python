import time

from waitress import serve
from flask import Flask
from threading import Event, Thread
from time import sleep


APP = Flask(__name__)


@APP.route('/')
def index():
    return "WebSocket Server Running"


def start_socket() -> None:
    # TODO: Confirm this is the place to listen from
    serve(APP, listen='0.0.0.0:5000')


def start_socket_thread(stop_event: Event) -> None:
    server_thread = Thread(target=start_socket, daemon=True)
    server_thread.start()

    while not stop_event.is_set():
        time.sleep(1)
