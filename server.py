import socket
import threading

# global variables...
PORT = 80 # random unused port on this PC, could be anything above 4000
SERVER = socket.gethostbyname(socket.gethostname()) # local IP of this PC
#SERVER = "0.0.0.0"
ADDR = (SERVER, PORT) # socket information
HEADER = 64 # integer that's used to get the size of the message that will be received/sent
FORMAT = 'utf-8' # thats the format it better stay like that
DISCONNECT_MESSAGE = "!DISCONNECT" #message used for disconnecting...

#here the socket of the server is made it's called 'server'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates the socket
server.bind(ADDR) # initializes the socket

# function that handles one client
# 'conn' is the socket of the client
# 'addr' is tuole of (IP of the client)
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()

