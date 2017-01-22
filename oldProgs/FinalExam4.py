import turtle

def rightUpperSquare(aTurtle, lowerX, lowerY, width):
    aTurtle.up()
    aTurtle.goto(lowerX, lowerY)
    aTurtle.down()
    for side in range(4):
         aTurtle.right(90)
         aTurtle.forward(width)

def leftUpperSquare(aTurtle, lowerX, lowerY, width):
    aTurtle.up()
    aTurtle.goto(lowerX, lowerY)
    aTurtle.down()
    for side in range(4):
         aTurtle.left(90)
         aTurtle.forward(width)

def recursive_squaresR(aTurtle, lowerX, lowerY, width, level):
    if (level > 0):
          rightUpperSquare(aTurtle, lowerX, lowerY, width)
          recursive_squaresR(aTurtle, lowerX, lowerY, width /3, level - 1)

def recursive_squaresL(aTurtle, lowerX, lowerY, width, level):
    if (level > 0):
          leftUpperSquare(aTurtle, lowerX, lowerY, width)
          recursive_squaresL(aTurtle, lowerX, lowerY, width /3, level - 1)

squares = turtle.Turtle()
squares.speed(0)
squares.hideturtle()
squares.color("coral")
recursive_squaresR(squares, 200, 200, 400, 6)
recursive_squaresL(squares, 200, -200, 400, 6)
