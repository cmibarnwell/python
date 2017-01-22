#Polygon Creator program written by Caleb Barnwell
#Computer Science, 09-26-15
import turtle
wn = turtle.Screen()
epic=turtle.Turtle()
side=input("How many sides are there?")
side=int(side)
length=input("How long should the sides be?")
length=int(length)
float(length)
turtcolor=input("What is the color?")
fillingcolor=input("What should the fill color be?")
epic.color(turtcolor)
epic.fillcolor(fillingcolor)

epic.begin_fill()
for i in range(side):
    epic.forward(length)
    epic.left(360/side)
epic.end_fill()

epic.ht()
       
wn.exitonclick()
