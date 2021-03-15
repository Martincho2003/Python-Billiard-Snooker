# client script
import socket 
import sys

# global variables...
PORT = 8080 # port of the server PC
SERVER_IP = "192.168.56.1" # local IP of the CURRENT server PC
#SERVER_IP = "213.191.161.44" # PUBLIC IP OF THE CURRENT SERVER
ADDRES = (SERVER_IP, PORT) # server socket information
BUFFER = 1024 # it's used to get the size of the message that will be sent/received
FORMAT = 'utf-8' # thats the format it better stay like that
DISCONNECT_MESSAGE = "!DISCONNECT" # message used for disconnecting...

# these lines make socket named 'client' and connect it to the server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket
    client_socket.connect(ADDRES) # connects it to the server socket
except Exception as e:
    print("Server is down or something..")
    print(e)
    exit(0)

def send(msg):
    try:
        client_socket.send(msg.encode(FORMAT))
        print(client_socket.recv(BUFFER).decode(FORMAT))
    except Exception as e:
        print("Server is down or something..")
        print(e)
        client_socket.close()
        exit(0)

def receive():
    try:
        msg = client_socket.recv(BUFFER).decode(FORMAT)
        print(f"[MESSAGE] {msg}")
        client_socket.send("Message received".encode(FORMAT))
        if msg == DISCONNECT_MESSAGE:
            client_socket.close()
            exit(0)
            
        return msg
    except Exception as e:
        print(e)
        exit(0)

def handle_():
    connected = True
    while connected:  
        if not receive():
            connected == False

handle_()

'''
# test samples
send("Hello!")

sth = input("say sth: ")
send(sth)

sth = input("say bye: ")
send(sth)

# finaly a disconnect message to end the connection
send(DISCONNECT_MESSAGE)
'''
