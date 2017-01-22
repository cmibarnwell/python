#Draw 5 Stars program written by Caleb Barnwell
#Computer Science, 10-18-15
import turtle
wn = turtle.Screen()
epic=turtle.Turtle()

def drawStar(t):
    for i in range(5):
        t.forward(110)
        t.left(216)

def draw5Stars(t):
    for i in range(5):
        drawStar(t)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

epic.left(180)
epic.forward(100)
epic.right(180)
draw5Stars(epic)
    

wn.exitonclick()
