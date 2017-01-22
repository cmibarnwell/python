#Turtle Documentation program written by Caleb Barnwell
#Computer Science, 10-25-15
import turtle

epic= turtle.Turtle()
epic2=epic.clone()
wn=turtle.Screen()

epic.forward(100)
epic.left(90)
epic.forward(75)

epic2.left(180)
epic2.forward(100)
epic2.left(90)
epic.forward(75)

epic.circle(15)
epic2.circle(15)

epic.home()
epic2.home()

epic.forward(50)
epic2.forward(50)

wn.exitonclick()
