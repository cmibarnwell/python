#Spiral Square program written by Caleb Barnwell
#Computer Science, 10-01-15

import turtle
wn=turtle.Screen()
epic=turtle.Turtle()

for i in range(26, 751, 25):
    epic.forward(i)
    epic.left(90)

wn.exitonclick()
