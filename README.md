# Turtle_lib
Python Library - Turtle

Overview - Python's Turtle Graphics provides a physical illustration of a virtual "turtle" that draws on a screen, allowing for interactive, real-time visual feedback while learning programming concepts. It was made with education in mind, which makes it perfect for classroom instruction. It makes graphical output more accessible to programmers who require simple visualizations by streamlining it without adding extra library overhead. This user-friendly tool helps students understand the foundations of programming and opens the door to more complex graphical programming.

Starting a turtle environment - from turtle import *
(Please install the Tk interface package on your computer if you encounter the error "No module named '_tkinter'.")

basics.py

explanation -  Basic turtle graphics methods include forward(), backward(), right(), left(), penup(), pendown(), speed(), color(), bgcolor(), and reset(). These commands control the turtle's movement, pen state, speed, and colors, enabling the creation of various shapes and patterns on the canvas.

draw_a_dashed_line.py

explanation - In turtle graphics, the drawing state is controlled by these pen control techniques.

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

















