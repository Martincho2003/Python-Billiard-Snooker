import socket

# global variables...
PORT = 80 # port of the server PC
#SERVER = "192.168.56.1" # local IP of the CURRENT server PC
SERVER = "213.191.161.44" # PUBLIC IP OF THE CURRENT SERVER
ADDR = (SERVER, PORT) # server socket information
HAEDER = 64 # it's used to get the size of the message that will be sent/received
FORMAT = 'utf-8' # thats the format it better stay like that
DISCONNECT_MESSAGE = "!DISCONNECT" # message used for disconnecting... 

# these lines make socket named 'client' and connect it to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket
client.connect(ADDR) # connects it to the server socket

# function that sends string(for now) to the server 
# msg - string we want to send
def send(msg):
    message = msg.encode(FORMAT) # encoding the massage
    msg_length = len(message) # getting its length
    send_length = str(msg_length).encode(FORMAT) # encoding the length
    send_length += b' ' * (HAEDER - len(send_length)) # preparing the length to be sent 
    client.send(send_length) # sending the length
    client.send(message) # sending the message

    # server still dont have a proper send function so the receive is just this
    # 1024 servs the purpose of message_length
    print(client.recv(1024).decode(FORMAT))

# LOGIC SHOUL BE IMPLEMENTED HERE

# TEST MESSAGES, input() is waiting for enter to be pressed befor the next message is sent
send("Hello world!")
input()
send("Hello everyone!")
input()
send("Bye :D!")
# finaly a disconnect message to end the connection
send(DISCONNECT_MESSAGE)