#Value Error program written by Caleb Barnwell
#Computer Science, 10-11-15

def drawEquitriangle(t, sz):
    """Creates an Equilateral Triangle with a turtle and size value."""
    for i in range(3):
        t.forward(sz)
        t.left(360/3)

import turtle
wn=turtle.Screen()
epic=turtle.Turtle()

drawEquitriangle(epic, 50)
