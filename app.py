import socket
import threading
import queue
from flask import Flask

PORT = 5050
SERVER = ''
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(ADDR)

app = Flask(__name__)

@app.route('/')
def server():
    return('server works or something(hopefully)')
    


