import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    while True:
        print(client.recv(2048).decode(FORMAT))

thread = threading.Thread(target = receive)
thread.start()

def enter():
    while True:
        message = (input(""))
        send(message)
        if message == DISCONNECT_MESSAGE:
            break

thread_2 = threading.Thread(target = enter)
thread_2.start()