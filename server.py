import socket
import threading
import queue

PORT = 80
SERVER = ''
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(ADDR)

def receive(conn, addr):
    connected = True
    while connected:
        message_len = conn.recv(HEADER).decode(FORMAT)
        if message_len:
            message_len = int(message_len)
            message = conn.recv(message_len).decode(FORMAT)
        #print (message)
        #print(addr)
        #print(conn)
        #conn.send("[MESSAGE RECEIVED]".encode(FORMAT))
        try:
            messages.put((message, addr, conn))
        except:
            print("failed")

def broadcast():
    while True:
        while not messages.empty():
            message, addr, conn = messages.get()
            #print(message)
            if conn not in clients:
                clients.append(conn)
                print("added!")
            for client in clients:
                #print(client)
                print (addr)
                client.send(f"<{str(addr)}> {message}".encode(FORMAT))
                print(message)

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = receive, args = (conn, addr))
        thread.start()
        thread_brdcst = threading.Thread(target = broadcast)
        thread_brdcst.start()
        
start()
