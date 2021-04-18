# server script
import socket
import threading
import sys 
import time
import pickle
import sqlite3
import hashlib


# flags
PORT = 9001 # random unused port on this PC, could be anything above 4000
#SERVER_IP = socket.gethostbyname(socket.gethostname()) # local IP of this PC
SERVER_IP = ""
ADDRES = (SERVER_IP, PORT) # socket information
BUFFER = 1024 # integer that's used to get the size of the message that will be received/sent
FORMAT = 'utf-8' # thats the format it better stay like that
DISCONNECT_MESSAGE = "!DISCONNECT" #message used for disconnecting...
CONFIRM_MESSAGE = "!CONFIRMED" # message used for confirming...
ERROR_MESSAGE = "!ERROR" # message used for error...

#here the socket of the server is made it's called 'server'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates the socket
server_socket.bind(ADDRES) # initializes the socket 

def create_table():
    connection = sqlite3.connect('User.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE if not exists Users (id INTEGER primary key autoincrement not null, Username VARCHAR(50) not null unique, Password VARCHAR(50) not null, wins INTEGER default 0, loses INTEGER default 0)')
    connection.commit()
    cursor.close()


'''
def receive_pickle(client_socket):
    try:
        msg = client_socket.recv(BUFFER)
        msg = pickle.loads(msg)

        client_socket.send(.encode(FORMAT))
        if msg == DISCONNECT_MESSAGE:
            client_socket.close()
            return False
            
        return msg
    except Exception as e:
        print("Client is down or something..")
        print(e)
        return False

'''





list_of_clients = [] # list of cients
game_list = []

# function that handles one client connection
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.") # indication message

    connected = True
    while connected:
        try:
            message = client_socket.recv(BUFFER)
            message = pickle.loads(message)
        except Exception as e:
            connected = False

    #print(first_message)
        check_receive(client_socket, message)



def check_receive(client_socket, msg):
    if msg[0] == "register":
        try:
            connection = sqlite3.connect('User.db')
            cursor = connection.cursor()
            cursor.execute('Insert Into Users(Username, Password) Values (?, ?)', (msg[1], msg[2]))
            connection.commit()
            cursor.close()
            #check_register = 1
            client_socket.send(pickle.dumps(CONFIRM_MESSAGE))
        except sqlite3.Error as e:
            error_msg = [ERROR_MESSAGE, e]
            error_msg = pickle.dumps(error_msg)
            client_socket.send(error_msg)

    elif msg[0] == "login":
        try:
            connection = sqlite3.connect('User.db')
            cursor = connection.cursor()
            cursor.execute('Select Password from Users where Username like ?;', [msg[1]])
            list = cursor.fetchall()
            recieved_tuple = list[0]
            if recieved_tuple[0] == "":
                error_msg = [ERROR_MESSAGE, "The username is not found!"]
                error_msg = pickle.dumps(error_msg)
                client_socket.send(error_msg)
            client_socket.send(pickle.dumps(CONFIRM_MESSAGE))
        except Exception as e:
            error_msg = [ERROR_MESSAGE, e]
            error_msg = pickle.dumps(error_msg)
            client_socket.send(error_msg)

    elif msg[0] == "create":
        check_name = 1
        for name in game_list:
            if name[0] == msg[1]:
                error_msg = [ERROR_MESSAGE, "This game already exists!"]
                error_msg = pickle.dumps(error_msg)
                client_socket.send(error_msg)
                check_name = 0

        if check_name == 1:
            game_list.append([msg[1], client_socket])
            client_socket.send(pickle.dumps(CONFIRM_MESSAGE))
            print(game_list)

    elif msg[0] == "join":
        check_name = 0
        for name in game_list:
            if name[0] == msg[1]:
                game(name[1], client_socket)
                client_socket.send(pickle.dumps(CONFIRM_MESSAGE))
                check_name = 1

        if check_name == 0:
            error_msg = [ERROR_MESSAGE, "This game does not exist!"]
            error_msg = pickle.dumps(error_msg)
            client_socket.send(error_msg)
            check_name = 0

def game(player1, player2):
    print("started game")

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

create_table()
start() # call of the function start()



