#Draw Sprite program written by Caleb Barnwell
#Computer Science, 10-28-15

import turtle

def drawSprite(t):
    for i in range(15):
        t.right(360/15)
        t.forward(120)
        t.stamp()

        t.right(180)
        t.forward(120)
        t.right(180)
    t.shape(circle)

def main():
    epic=turtle.Turtle()
    wn=turtle.Screen()
    drawSprite(epic)
    epic.speed(5)

main()
