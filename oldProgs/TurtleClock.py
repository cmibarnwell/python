#Turtle Clock program written by Caleb Barnwell
#Computer Science, 10-01-15

import turtle
wn = turtle.Screen()
epic=turtle.Turtle()

epic.shape("turtle")
epic.color("blue")
wn.bgcolor("green")

epic.stamp()

for i in range(12):
    epic.penup()
    epic.forward(100)
    epic.pendown()
    epic.forward(15)
    epic.penup()
    epic.forward(15)
    epic.stamp()
    epic.backward(130)
    epic.right(360/12)

wn.exitonclick()
