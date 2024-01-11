Add Players
=================




In this activity, you will learn to add a functionality to login more than two players to the game.




Follow the given steps to complete this activity:
	
1. Accept every connection as a new player to the game.


* Open the file `server.py`.


* Go to method accept_connections() and comment the if-else statement to define the player type as player1 and player2 for every new connection.
~~~python
# if(len(CLIENTS.keys()) == 0):
#     CLIENTS[player_name] = {'player_type' : 'player1'}
# else:
#     CLIENTS[player_name] = {'player_type' : 'player2'}
~~~


* Concatenate length of CLIENTS with string 'player' and store it in player_num variable.
~~~python
player_num = 'player'+ str(len(CLIENTS))
~~~


* Set value of 'player_type' key in the CLIENTS dictionary to player_num.
~~~python
CLIENTS[player_name] = {'player_type' : player_num}
~~~


* Save and run the code to check the output.
