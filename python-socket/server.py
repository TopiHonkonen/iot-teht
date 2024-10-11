import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"

ADDR = (SERVER, PORT)
FORMAT = "ascii"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length.strip())
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"{addr} says: {msg}")
            message = "Received message".encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b" " * (HEADER - len(send_length))
            conn.send(send_length)
            conn.send(message)
        else:
            connected=False
            print(f"{addr} disconnected")
    conn.close()

server.listen()
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
