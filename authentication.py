from tkinter import *
import sqlite3
import hashlib
import socket 
import sys
import pickle

window = Tk()
window.title('Billiard game')
window.geometry('500x500')
window.configure(background="Green")
check_login = 0
check_register = 0


PORT = 8080 # port of the server PC
SERVER_IP = "127.0.1.1" # local IP of the CURRENT server PC
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

def send_starting_game_message():
    try:
        sth = ["Starting game", client_socket]
        msg = pickle.dumps(sth)
        client_socket.send(msg)
    except Exception as e:
        print("Server is down or something..")
        print(e)
        client_socket.close()
        exit(0)   

def receive():
    try:
        msg = client_socket.recv(BUFFER).decode(FORMAT)
        sth = pickle.loads(msg)
        for i in sth:
                #msg_to_pickle = ["Let's start", client_socket]
            print(f"[MESSAGE] {i}")
        #client_socket.send("Message received".encode(FORMAT))
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

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

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

def create_table():
    connection = sqlite3.connect('User.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE if not exists Users (id INTEGER primary key autoincrement not null, Username VARCHAR(50) not null unique, Password VARCHAR(50) not null, wins INTEGER default 0, loses INTEGER default 0)')
    connection.commit()
    cursor.close()

def register(username, pasword):
    if username.get() == "" or pasword.get() == "":

        register_page()
    else:
        password = hash_password(pasword.get())
        try:
            connection = sqlite3.connect('User.db')
            cursor = connection.cursor()
            cursor.execute('Insert Into Users(Username, Password) Values (?, ?)', (username.get(), password))
            connection.commit()
            cursor.close()
            check_register = 1
        except sqlite3.Error as e:
            err_window = Tk()
            err_window.title("Error")
            err_window.geometry('500x200')
            err_window.configure(background="Red")
            error = StringVar(err_window)
            error.set(e) 
            Label(err_window, text="An error occurred: " + error.get() + "\n Please try again!").pack()
            Button(err_window, text='Close', command=err_window.destroy).pack()
    
    if check_register == 1:
        starting_page(check_register)
    else:
        register_page()

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

def login(username, password):
    connection = sqlite3.connect('User.db')
    cursor = connection.cursor()
    cursor.execute('Select Password from Users where Username like ?;', [username.get()])
    list = cursor.fetchall()
    recieved_tuple = list[0]
    if recieved_tuple[0] == "":
        err_window = Tk()
        err_window.title("Error")
        err_window.geometry('500x200')
        err_window.configure(background="Red")
        Label(err_window, text="An error occurred:\nThe username is not found! \n Please try again!").pack()
        Button(err_window, text='Close', command=err_window.destroy).pack()
        cursor.close()
        login_page()
    else:
        if(recieved_tuple[0] == hash_password(password.get())):
            starting_game_page()
        else:
            err_window = Tk()
            err_window.title("Error")
            err_window.geometry('500x200')
            err_window.configure(background="Red")
            Label(err_window, text="An error occurred:\nWrong password!\nPlease try again!").pack()
            Button(err_window, text='Close', command=err_window.destroy).pack()
            login_page()

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

def starting_game_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(3, weight=1)
    Button(window, text="Create game", command="""TODO""").grid(row=1, column=1)
    Button(window, text="Join game", command=join_game_page).grid(row=3, column=1)

def join_game_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(1, weight=1)
    server_code = StringVar(window)
    Entry(window, textvariable=server_code).grid(row=1, column=1)
    Button(window, text="Join game", command=join_game).grid(row=1, column=2)

def create_game_page():
    for widget in window.winfo_children():
        widget.destroy()
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(1, weight=1)
    server_code = StringVar(window)
    Entry(window, textvariable=server_code).grid(row=1, column=1)
    Button(window, text="Create game", command= lambda: create_game(server_code)).grid(row=1, column=2)

def join_game():
    send_starting_game_message()
    window.destroy() #if success

def main():
    create_table()
    starting_page(check_register)
    window.mainloop()

main()