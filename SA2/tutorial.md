Resize the Game Canvas
===========================


In this activity, you will learn to resize the game canvas and its elements to fit the screen size.

<img src= "https://media.slid.es/uploads/1525693/images/10883190/SA2.png” width = "480" height = "320">

Follow the given steps to complete this activity:


1. Get the width and height of the device screen.


* Open the file `client.py` and go inside the method ask_player_name(). 
* Fetch and store the screen width and screen height in two different variables.
~~~sh
screen_width = name_window.winfo_screenwidth()
screen_height = name_window.winfo_screenheight()
~~~


2. Resize the Canvas to fit the screen. 


* Resize the Canvas and Image as per the size of the screen.


~~~sh
image = image.resize((screen_width, screen_height))
 	canvas1 = Canvas( name_window, width = screen_width,height = screen_width)
~~~
3. Make text responsive


* Create responsive font size and position for different text on the login screen.
~~~sh
font_size = int(screen_width * 0.03)
 	canvas1.create_text( screen_width/2, screen_height/5 , text = "Enter Name", font=("Chalkboard SE", font_size), fill="white")
~~~


* Save and run the code to check the output.
