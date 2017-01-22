#Find Hypotenuse program written by Caleb Barnwell
#Computer Science, 11-01-15

def findHypot(a,b):
    c=((a**2)+(b**2))**(1/2)
    print(c)

side1=int(input("What is the triangle's first side length?"))
side2=int(input("What is the triangle's second side length?"))

findHypot(side1, side2)
