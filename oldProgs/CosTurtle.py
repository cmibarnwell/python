#Cos Turtle program written by Caleb Barnwell
#Computer Science, 10-26-15

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
turtle.setworldcoordinates(-25,-1.5,385,1.5)
epic = turtle.Turtle()
epic.speed(10)

def drawPlot(t):
    t.goto(0,-1.25)
    t.left(90)
    for i in range(50):
        t.forward(.05)
        t.right(90)
        t.forward(2.5)
        t.backward(2.5)
        t.left(90)
    t.right(90)
    for i in range(72):
        t.forward(5)
        t.right(90)
        t.forward(.025)
        t.backward(.025)
        t.left(90)
    t.right(90)
    for i in range(50):
        t.forward(.05)
        t.right(90)
        t.forward(2.5)
        t.backward(2.5)
        t.left(90)
    t.right(90)
    for i in range(72):
        t.forward(5)
        t.right(90)
        t.forward(.025)
        t.backward(.025)
        t.left(90)

def cosLine(t):
    for i in range(360):
        cosval1=math.cos(math.radians(i))
        t.goto(i,cosval1)

drawPlot(epic)
cosLine(epic)

wn.exitonclick()
