from tkinter import *
import sqlite3
import hashlib
import tkinter

connection = sqlite3.connect('User.db')
cursor = connection.cursor()

window = Tk()
window.title('Billiard game')
window.geometry('500x500')
window.configure(background="Green")
check_login = 0
check_register = 0

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
    cursor.execute('CREATE TABLE if not exists Users (id INTEGER primary key autoincrement not null, Username VARCHAR(50) not null unique, Password VARCHAR(50) not null, wins INTEGER default 0, loses INTEGER default 0)')
    connection.commit()

def register(username, pasword):
    if username.get() == "" or pasword.get() == "":

        register_page()
    else:
        password = hash_password(pasword.get())
        try:
            cursor.execute('Insert Into Users(Username, Password) Values (?, ?)', (username.get(), password))
            connection.commit()
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

def login(username, password):
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
        login_page()
    else:
        if(recieved_tuple[0] == hash_password(password.get())):
            window.destroy()
            #starting game
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

def main():
    create_table()
    starting_page(check_register)
    window.mainloop()

main()