# Turtle_lib
Python Library - Turtle

Overview - Python's Turtle Graphics provides a physical illustration of a virtual "turtle" that draws on a screen, allowing for interactive, real-time visual feedback while learning programming concepts. It was made with education in mind, which makes it perfect for classroom instruction. It makes graphical output more accessible to programmers who require simple visualizations by streamlining it without adding extra library overhead. This user-friendly tool helps students understand the foundations of programming and opens the door to more complex graphical programming.

Starting a turtle environment - from turtle import *
(Please install the Tk interface package on your computer if you encounter the error "No module named '_tkinter'.")

basics.py

Explanation -  Basic turtle graphics methods include forward(), backward(), right(), left(), penup(), pendown(), speed(), color(), bgcolor(), and reset(). These commands control the turtle's movement, pen state, speed, and colors, enabling the creation of various shapes and patterns on the canvas.

draw_a_dashed_line.py

Explanation - In turtle graphics, the drawing state is controlled by these pen control techniques.

Pen control (Drawing state )

pendown() | pd() | down() - The turtle can draw lines because "pendown()" lowers the pen
penup() | pu() | up() -  "penup()" lifts the pen, preventing drawing.
pensize() | width() - "pensize()" sets the thickness of lines drawn.
pen() - "pen()" combines color and width settings.
isdown()  - "isdown()" checks if the pen is down. 

draw_shapes.py

Explanation - The drawing colors in Turtle Graphics are controlled by these color control techniques. 

Color control
color() - "color()" simultaneously sets the fill and pen colors. 
pencolor() - "pencolor()" sets the color of the pen for drawing lines. 
fillcolor() -  The color that fills shapes is set by the "fillcolor()" function. 
These commands make it easier to change the color of lines and shapes, which improves the drawings made with the turtle module in terms of appearance.

random_walk.py

Explanation - We are using setheading() and speed (). we are importing random module as well 

speed()  - The turtle's speed can be changed with the "turtle.speed()" method, which takes speedstrings like "fastest" and "slowest" in addition to numbers between 0 and 10.
Motion stops at speed 0, but animation speed increases from 1 to 10.
Current speed is returned without argument. "Fastest" (0), "fast" (10), "normal" (6), "slow" (3), and "slowest" (1) are the speeds that are mapped to speedstrings.
Turtle graphics programming can now be more easily visualized thanks to this method of precisely adjusting animation speed for smooth or instantaneous movement.

setheading() - The turtle's orientation can be adjusted to a given angle in degrees using the "turtle.setheading()" or "turtle.seth()" methods.
Common directions include 0 for east, 90 for north, 180 for west, and 270 for south. 
It simplifies controlling the turtle's direction, allowing precise orientation adjustments for drawing shapes and navigating the canvas. 
After setting the heading, "turtle.heading()" returns the current orientation angle.

move_forward.py

You can focus on the TurtleScreen to gather important events by using these Turtle module calls. Turtle.onkey() binds a function to a key press event, Turtle.onkeyrelease() binds a function to a key release event, and turtle.listen() focuses on the screen. These features allow keyboard inputs to be used to interact with the turtle images.


different_directions.py

(Pen control)
More drawing control from turtle
reset() - The Turtle module's reset() function clears the screen in addition to returning the turtle's location, direction, and other properties to their initial values. 
clear() - The turtle.clear() function does not move the turtle or change the locations or drawings of other turtles; instead, it removes only the turtle's drawings from the screen.
write() - The turtle.write() function uses the supplied font and aligns text on the TurtleScreen at the current turtle position ("left", "center", or "right"). After writing, the pen goes to the lower-right corner of the text if move is set to True.


 Turtle's position - The home() function returns the turtle to its initial location in the middle of the screen. The home position of the turtle is at (0, 0), and you may use pos() to get its current position. You can use clearscreen() to start over by erasing the entire window. Resetting the drawing environment and controlling the turtle's location are made easier with the help of these functions.














