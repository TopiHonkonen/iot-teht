import socket

HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"

ADDR = (SERVER, PORT)
FORMAT = "ascii"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length.strip())
        msg = client.recv(msg_length).decode(FORMAT)
        print(msg)

send("testing")
client.close()
