# server script
import socket
import threading
import sys  


# flags
PORT = 8080 # random unused port on this PC, could be anything above 4000
SERVER_IP = socket.gethostbyname(socket.gethostname()) # local IP of this PC
#SERVER_IP = "0.0.0.0"
ADDRES = (SERVER_IP, PORT) # socket information
BUFFER = 1024 # integer that's used to get the size of the message that will be received/sent
FORMAT = 'utf-8' # thats the format it better stay like that
DISCONNECT_MESSAGE = "!DISCONNECT" #message used for disconnecting...

#here the socket of the server is made it's called 'server'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates the socket
server_socket.bind(ADDRES) # initializes the socket

list_of_clients = [] # list of cients 
           
def receive(client_socket, addr):
    try:
        msg = client_socket.recv(BUFFER).decode(FORMAT)
        print(f"[{addr}] {msg}")
        client_socket.send("Message received".encode(FORMAT))
        if msg == DISCONNECT_MESSAGE:
            client_socket.close()
            return False
            
        return msg
    except Exception as e:
        print(e)
        return False

def send(client_socket, msg):
    try:
        client_socket.send(msg.encode(FORMAT))
        print(client_socket.recv(BUFFER).decode(FORMAT))
    except Exception as e:
        print("Server is down or something..")
        print(e)
        client_socket.close()


'''
# function that handles one client connection
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.") # indication message

    connected = True
    while connected:
        if not receive(client_socket, addr):
            connected = False
'''
# function that handles one client connection
def handle_client(client_socket, addr):
    # test samples
    send(client_socket, "Hello!")

    sth = input("say sth: ")
    send(client_socket, sth)

    sth = input("say bye: ")
    send(client_socket, sth)

    # finaly a disconnect message to end the connection
    send(client_socket, DISCONNECT_MESSAGE)

# function that runs the server
def start():
    server_socket.listen() # server socket starts to look for connections with other sockets
    print(f"[LISTENING] Server is listening on {ADDRES}") # indication message
    while True: # the server works untill its shut down
        client_socket, addr = server_socket.accept() # if a socket(client) tries to connect it gets accepted
        list_of_clients.append(client_socket)
        client_thread = threading.Thread(target = handle_client, args = (client_socket, addr)) # a new thread is made for every client, 'handle_client' function is called
        client_thread.start() # the just created thread is started, client can communicate with the server
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # indication message

print("[STARTING] server is starting...") # indication message
start() # call of the function start()

