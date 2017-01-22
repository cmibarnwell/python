#Random Rectangle Generator program written by Caleb Barnwell
#Computer Science, 11-8-15

import turtle
import random
wn=turtle.Screen()
epic=turtle.Turtle()
turtle.setworldcoordinates(-100,-100,100,100)
wn.bgcolor("black")
epic.speed(7)
turtle.colormode(255)

def randoRectangle(t,l,w):
    length1=random.randrange(5,l)
    width1=random.randrange(2,w)
    positionx=random.randrange(-80,80)
    positiony=random.randrange(-80,80)
    red=random.randrange(0,255)
    green=random.randrange(0,255)
    blue=random.randrange(0,255)
    fcolor= red,green,blue
    t.fillcolor(fcolor)
    t.begin_fill()
    t.forward(length1)
    t.right(90)
    t.forward(width1)
    t.right(90)
    t.forward(length1)
    t.right(90)
    t.forward(width1)
    t.right(90)
    t.penup()
    t.goto(positionx, positiony)
    t.pendown()
    t.end_fill()

def rectRepeater(t,l,w,r):
    for i in range(r):
        randoRectangle(t,l,w)

rectNum=int(input("What is the desired amount of random rectangles? "))
length=int(input("What is the desired max length of the random rectangles? "))
width=int(input("What is the desired max width of the random rectangles? "))

maxLength=max(10,length)
maxWidth=max(10,width)

rectRepeater(epic, maxLength, maxWidth, rectNum)
epic.hideturtle()

wn.exitonclick()
