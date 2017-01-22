#Star Turtle program written by Caleb Barnwell
#Computer Science, 09-26-15
import turtle
wn = turtle.Screen()
epic=turtle.Turtle()
wnbgcolor=input("What is the background color?")
turtcolor=input("What is the pen color?")
size=input("What is the size of the pen?")
int(size)
wn.bgcolor(wnbgcolor)
epic.color(turtcolor)
epic.pensize(size)

for i in range(5):
    epic.forward(110)
    epic.left(216)
wn.exitonclick()
