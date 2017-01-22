#Dirt House program written by Caleb Barnwell
#Computer Science, 11-8-15

import turtle
wn=turtle.Screen()
epic=turtle.Turtle()
epic.fillcolor("brown")
epic.speed(7)

def Block(t):
    t.begin_fill()
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()

def fourBlockSquare(t):
    Block(t)
    epic.forward(20)
    Block(t)

    epic.penup()
    epic.left(90)
    epic.forward(20)
    epic.left(90)
    epic.forward(20)
    epic.left(180)
    epic.pendown()
    Block(t)

    epic.penup()
    epic.forward(20)
    epic.pendown()
    Block(t)

fourBlockSquare(epic)

epic.penup()
epic.goto(0,40)
epic.pendown()

fourBlockSquare(epic)

epic.penup()
epic.goto(40,80)
epic.pendown()

fourBlockSquare(epic)

epic.penup()
epic.goto(80,40)
epic.pendown()

fourBlockSquare(epic)

epic.penup()
epic.goto(80,0)
epic.pendown()

fourBlockSquare(epic)

epic.penup()
epic.goto(40,0)
epic.pendown()

epic.fillcolor("tan")
fourBlockSquare(epic)

epic.penup()
epic.goto(40,40)
epic.pendown()

fourBlockSquare(epic)

t.goto(60,120)

def whiteFlag(t):
    t.left(90)
    t.forward(20)
    t.right(135)
    t.forward(12)
    t.right(125)
    t.forward(15)

whiteFlag(epic)
wn.exitonclick()
