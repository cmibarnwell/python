import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.random()
    if 0 <= coin <=.17:
        t.left(0)
    elif .17 < coin <=.34:
        t.left(120)
    elif .34 < coin <=.51:
        t.left(180)
    elif .51 < coin <=.68:
        t.left(240)
    elif .68 < coin <=.84:
        t.left(300)
    else:
        t.left(60)


    t.forward(20)

wn.exitonclick()
