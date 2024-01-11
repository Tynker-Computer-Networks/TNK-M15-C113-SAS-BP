Save Player’s Information
===================


In this activity, you will learn to assign player_type to the new player and store its details on the server.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/783d4aa3-59d8-428b-831c-797f3ad050d4.gif" width = "480" height = "320">


Follow the given steps to define functions to send and receive player information and store it on the server.


1. Send the new player name to the server.
* Open the file `client.py`.
* Define a method to save the player name and send it to the server.
~~~python
def save_name():
    global SERVER, player_name, name_window, name_entry
    player_name = name_entry.get()
    name_entry.delete(0, END)
    name_window.destroy()
    SERVER.send(player_name.encode())
    button = Button(name_window, text="Save", font=("Chalkboard SE", font_size), command=save_name, height=1, bg="#80deea", bd=3)
~~~
2. Receive the player name from the client.
* Open the file `server.py`.
* Receive the player name from the client on connection, decode it, and store it in a variable.
~~~python
player_name = player_socket.recv(1024).decode().strip()
~~~


3. Assign the player type to the new player.
* Assign the player type to the new player on the basis of the number of players already joined.
~~~python
if(len(CLIENTS.keys()) == 0)   
      CLIENTS[player_name] = {'player_type': 'player1'}
 else:
      CLIENTS[player_name] = {'player_type': 'player2'}
~~~


4. Save player information on the server.


* Save the new player information on the server and print the players details.
~~~python
CLIENTS[player_name]["player_socket"] = player_socket
CLIENTS[player_name]["address"] = addr
CLIENTS[player_name]["player_name"] = player_name
CLIENTS[player_name]["turn"] = False
 
print(f"Connection established with {player_name} : {addr}")
print(CLIENTS)
~~~


* Save and run the code to check the output.
