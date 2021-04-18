# client script
import socket 
import sys
import threading
import pickle
from tkinter import *
import hashlib
from game import run

# global variables...
PORT = 9001 # port of the server PC
#SERVER_IP = "127.0.1.1" # local IP of the CURRENT server PC
SERVER_IP = "" # PUBLIC IP OF THE CURRENT SERVER
ADDRES = (SERVER_IP, PORT) # server socket information
BUFFER = 1024 # it's used to get the size of the message that will be sent/received
FORMAT = 'utf-8' # thats the format it better stay like that
DISCONNECT_MESSAGE = "!DISCONNECT" # message used for disconnecting...
CONFIRM_MESSAGE = "!CONFIRMED" # message used for confirming...
ERROR_MESSAGE = "!ERROR" # message used for error...

# these lines make socket named 'client' and connect it to the server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket
    client_socket.connect(ADDRES) # connects it to the server socket
except Exception as e:
    print("Server is down or something..")
    print(e)
    exit(0)

window = Tk()
window.title('Billiard game')
window.geometry('500x500')
window.configure(background="Green")
check_login = 0
check_register = 0

def send_pickle(msg):
    try:
        msg = pickle.dumps(msg)
        client_socket.send(msg)
        recv_msg = client_socket.recv(BUFFER)
        recv_msg = pickle.loads(recv_msg)
        print(recv_msg)
        if recv_msg:
            return recv_msg
    except Exception as e:
        print("Server is down or something..")
        print(e)
        client_socket.close()
        exit(0)
'''
def receive():
    try:
        recv_msg = client_socket.recv(BUFFER)
        recv_msg = pickle.loads(recv_msg)


        print(f"[MESSAGE] {msg}")
        client_socket.send(CONFIRM_MESSAGE.encode(FORMAT))
        if msg == DISCONNECT_MESSAGE:
            client_socket.close()
            return False
        if msg == ERROR_MESSAGE:
            error_msg = client_socket.recv(BUFFER).decode(FORMAT)
            handle_error(error_msg)
            return False
     
        return msg
    except Exception as e:
        print("Server is down or something..")
        print(e)
        exit(0)
'''
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def handle_error(error_msg):
        err_window = Tk()
        err_window.title("Error")
        err_window.geometry('500x200')
        err_window.configure(background="Red")

        Label(err_window, text="An error occurred: \n" + str(error_msg) + "\n Please try again!").pack()
        Button(err_window, text='Close', command=err_window.destroy).pack()

def register(username, pasword):
    if username.get() == "" or pasword.get() == "":
        register_page()

    else:
        pasw = hash_password(pasword.get())
        register_list = ["register", username.get(), pasw]
        result = send_pickle(register_list)

        if result[0] == ERROR_MESSAGE:
            handle_error(result[1])
        else:
            starting_page(check_register)


def login(username, pasword):
    if username.get() == "" or pasword.get() == "":
        login_page()

    else:
        pasw = hash_password(pasword.get())
        login_list = ["login", username.get(), pasw] 
        result = send_pickle(login_list)
        
        if result[0] == ERROR_MESSAGE:
            handle_error(result[1])
        else:
            starting_game_page()



def register_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(2)
    Label(window, text="Uername:").grid(row=0, column=0)
    Label(window, text="Password:").grid(row=1, column=0)
    user = StringVar(window)
    Entry(window, textvariable=user).grid(row=0, column=1)
    pas = StringVar(window)
    Entry(window, textvariable=pas, show='*').grid(row=1, column=1)
    Button(window, text="Register", command= lambda: register(user, pas)).grid(row=3, column=1)
    Button(window, text="Back", command= lambda: starting_page(0)).grid(row=5, column=1)

def login_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(2)
    Label(window, text="Uername:").grid(row=0, column=0)
    Label(window, text="Password:").grid(row=1, column=0)
    user = StringVar(window)
    Entry(window, textvariable=user).grid(row=0, column=1)
    pas = StringVar(window)
    Entry(window, textvariable=pas, show='*').grid(row=1, column=1)
    Button(window, text="Login", command= lambda: login(user, pas)).grid(row=3, column=1)
    Button(window, text="Back", command= lambda: starting_page(0)).grid(row=5, column=1)

def starting_page(check_register):
    for widget in window.winfo_children():
        widget.destroy()
    if check_register == 1:
        Label(window, text="Registration successful", background="Green").grid(row=1, column=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(6, weight=1)
    if check_register == 0:
        Label(window, text='Welcome to our game', background="Green", font="26").grid(row=1, column=1)
    Label(window, background="Green").grid(row=2, column=1)
    Label(window, background="Green").grid(row=3, column=1)
    Button(window, text="Register", command=register_page).grid(row=4, column=1)
    Label(window, background="Green").grid(row=5, column=1)
    Button(window, text="Login", command=login_page).grid(row=6, column=1)

def starting_game_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(3, weight=1)
    Button(window, text="Create game", command=create_game_page).grid(row=1, column=1)
    Button(window, text="Join game", command=join_game_page).grid(row=3, column=1)

def join_game_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(1, weight=1)
    game_name = StringVar(window)
    Entry(window, textvariable=game_name).grid(row=1, column=1)
    Button(window, text="Join game", command= lambda: join_game(game_name)).grid(row=1, column=2)

def join_game(game_name):
    if game_name.get() == "":
        starting_game_page()

    else:
        register_list = ["join", game_name.get()]
        result = send_pickle(register_list)

        if result[0] == ERROR_MESSAGE:
            handle_error(result[1])
        else:
            window.destroy()
            run(client_socket)


def create_game_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(1, weight=1)
    server_code = StringVar(window)
    Entry(window, textvariable=server_code).grid(row=1, column=1)
    Button(window, text="Create game", command= lambda: create_game(server_code)).grid(row=1, column=2)

def create_game(game_name):
    if game_name.get() == "":
        starting_game_page()

    else:
        register_list = ["create", game_name.get()]
        result = send_pickle(register_list)

        if result[0] == ERROR_MESSAGE:
            handle_error(result[1])
        else:
            window.destroy()
            run(client_socket)

def main():
    starting_page(check_register)
    window.mainloop()

main()




