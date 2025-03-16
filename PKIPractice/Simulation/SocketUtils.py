from waitress import serve
from flask import Flask, send_from_directory
from threading import Event, Thread
from time import sleep

import sys
from os.path import abspath, dirname, join
script_dir = dirname(abspath(__file__))
if script_dir in ['PKI_Practice', 'PKI Practice', 'app']:
    sys.path.append(abspath(script_dir))
elif script_dir == 'PKIPractice':
    sys.path.append(abspath(join(script_dir, '..')))
else:
    sys.path.append(abspath(join(script_dir, '../..')))

from PKIPractice.Simulation.DBUtils import PKIDatabase


APP = Flask(__name__, static_folder="../../pki-front-end/dist")
APP_DATABASE = None


@APP.route('/')
def index():
    return send_from_directory(APP.static_folder, "index.html")


def start_socket() -> None:
    # TODO: Confirm this is the place to listen from
    serve(APP, listen='0.0.0.0:5000')


def start_socket_thread(stop_event: Event, db_object: PKIDatabase) -> None:
    # Set the database to be the db_object passed in
    global APP_DATABASE
    APP_DATABASE = db_object

    # Start the serving the WGSI application
    server_thread = Thread(target=start_socket, daemon=True)
    server_thread.start()

    while not stop_event.is_set():
        sleep(1)
