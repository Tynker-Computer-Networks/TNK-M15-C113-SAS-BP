Create a Game Canvas
============================


In this activity, you will learn to create the game canvas with a background image and a text label.


<img src= "https://media.slid.es/uploads/1525749/images/8837072/PRO-C204_Slide_No.14.gif" width = "480" height = "320">


Follow the given steps to complete this activity:


1. Create a Tkinter Image for the background


* Open the `client.py` file and go to the method ask_player_name.


* Open an image, resize it, and then convert it into a format that can be displayed in a Tkinter window.
~~~sh
image = Image.open("./assets/background.png")
image = image.resize((screen_width, screen_height))
bg = ImageTk.PhotoImage(image)
~~~
2. Create a canvas that occupies the entire screen to draw or place other widgets and graphics within it.


* Create a canvas object and use pack() method with fill=”both” to fill the entire screen.
~~~sh
canvas1 = Canvas(name_window, width = screen_width, height = screen_width)
canvas1.pack(fill = "both", expand = True)
~~~
3. Add an image and text to the canvas. 


* Use create_image() and create_text() methods of Tkinter’s Canvas object to add an image and text to the canvas.


~~~sh
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",font_size), fill="white")
~~~


* Save and run the code to check the output.
