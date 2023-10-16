import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None
CLIENTS = {}

def accept_connections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()

        player_name = player_socket.recv(1024).decode().strip()
            
        # Comment following    
        if(len(CLIENTS.keys()) == 0):
            CLIENTS[player_name] = {'player_type' : 'player1'}
        else:
            CLIENTS[player_name] = {'player_type' : 'player2'}

        # Concatenate length of CLIENTS with string 'player' and sav it in player_num variable
        
        # Set CLIENTS[player_name] to a dict with 'player_type' key and value player_num
        

        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addr
        CLIENTS[player_name]["player_name"] = player_name
        CLIENTS[player_name]["turn"] = False

        print(f"Connection established with {player_name} : {addr}")
        print(CLIENTS)

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** LUDO LADDER ***")

    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")

    accept_connections()

setup()
