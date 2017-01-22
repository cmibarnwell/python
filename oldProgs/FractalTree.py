#Fractal Tree Program written by Caleb Barnwell
#Computer Science, 12-13-15


import turtle
import random

def tree(branchLen,t):
    angle=random.randrange(15,45)
    if branchLen > 5:
        t.width(branchLen/10)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(angle)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
