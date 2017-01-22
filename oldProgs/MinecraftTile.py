#Minecraft Tile program written by Caleb Barnwell
#Computer Science, 10-04-15

import turtle
wn=turtle.Screen()
epic=turtle.Turtle()
epic.fillcolor("red")
epic.speed(3)

#Bottom half of Square
epic.begin_fill()
epic.penup()
epic.goto(-50,-20)
epic.pendown()
epic.forward(100)
epic.right(90)
epic.forward(30)
epic.right(90)
epic.forward(100)
epic.right(90)
epic.forward(30)
epic.end_fill()

#Top half of Square
epic.begin_fill()
epic.penup()
epic.goto(-50,20)
epic.right(90)
epic.pendown()
epic.forward(100)
epic.left(90)
epic.forward(30)
epic.left(90)
epic.forward(100)
epic.left(90)
epic.forward(30)
epic.end_fill()

#Rest of Square
epic.penup()
epic.goto(-50,-50)
epic.left(180)
epic.pendown()
for i in range(4):
    epic.forward(100)
    epic.right(90)

#T
epic.penup()
epic.goto(-50,15)
epic.right(90)
epic.forward(12.5)
epic.pendown()
epic.forward(12.5)
epic.right(90)
epic.forward(30)
epic.left(180)
epic.forward(30)
epic.right(90)
epic.forward(12.5)
epic.penup()

#N

epic.forward(5)
epic.right(90)
epic.forward(30)
epic.left(180)
epic.pendown()
epic.forward(30)
epic.goto(10, -15)
epic.forward(30)

#T(2)
epic.penup()
epic.right(90)
epic.forward(5)
epic.pendown()
epic.forward(12.5)
epic.right(90)
epic.forward(30)
epic.left(180)
epic.forward(30)
epic.right(90)
epic.forward(12.5)

epic.penup()
epic.forward(50)


wn.exitonclick()
