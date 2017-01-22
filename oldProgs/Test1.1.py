#Test 1.1 program written by Caleb Barnwell
#Computer Science, 10-18-15
import turtle

def drawCoralSquare(t):
    t.fillcolor("coral")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

def main():
    wn = turtle.Screen()
    epic=turtle.Turtle()
    drawCoralSquare(epic)

main()    
