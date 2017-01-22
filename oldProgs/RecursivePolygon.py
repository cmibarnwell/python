#Recursive Polygon program written by Caleb Barnwell
#Computer Science, 01-03-16
import turtle
wn = turtle.Screen()
epic=turtle.Turtle()
wn.colormode(255)
wn.bgcolor("violet")

length=50
side=11
r=-10
g=-25
b=-35
def draw_poly(side,length,r,g,b):
    while side>3:
        side=side-1
        r=int(r+10)
        g=int(g+25)
        b=int(b+35)
        epic.fillcolor(r,g,b)
        epic.begin_fill()
        for i in range(side):
            epic.forward(length)
            epic.left(360/side)
        epic.end_fill()
        draw_poly(side,length,r,g,b)
        break

draw_poly(side,length,r,g,b)
epic.ht()
       
wn.exitonclick()
