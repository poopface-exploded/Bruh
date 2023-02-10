import socket
import threading
import queue
from flask import Flask

app = Flask(__name__)

@app.route('/')
def server():
    return 'Hello, World!'
