Define Maximum Player Limit
==============


In this activity, you will learn to limit the number of players to four.


Follow the given steps to complete this activity:
1. Add a condition to check the number of players joined.
* Open the file `server.py`.


* Go to the accept_connections() and write an if statement to check if the length of clients added is less than 4.
~~~python
if(len(CLIENTS) < 4):
~~~


* Move the entire code under the if statement.
~~~python
player_num = 'player'+ str(len(CLIENTS))
      CLIENTS[player_name] = {'player_type' : player_num}
CLIENTS[player_name]["player_socket"] = player_socket
      CLIENTS[player_name]["address"] = addr
      CLIENTS[player_name]["player_name"] = player_name
      CLIENTS[player_name]["turn"] = False
      print(f"Connection established with {player_name} : {addr}")
      print(CLIENTS)
~~~


* Write the else statement to print “Maximum player limit reached”.
~~~python
else:
      print("Maximum Player Limit Reached")
~~~


* Save and run the code to check the output.
