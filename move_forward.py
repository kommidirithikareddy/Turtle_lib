from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(2)

screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()
