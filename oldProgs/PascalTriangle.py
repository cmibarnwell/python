# -----------------------------------------+
# Caleb Barnwell                           | 
# PascalsTriangle.py                       |
# Last Updated: December 13, 2014          |  
# -----------------------------------------|
# A program that creates Pascal's Triangle |  
# -----------------------------------------+

#Performs Calculations
def combination(n, k):
    if k==0 or n==k or n==0:
        return 1
    else:
        return combination(n-1,k)+combination(n-1,k-1)

#Sets up formatting   
def pascals_triangle(rows):
    for row in range(rows):
        answer = ""
        for column in range(row + 1):
            answer = answer + str(combination(row, column)) + "\t"
        print(answer)

#Asks user for intended size
length=int(input("How large would you like your pascal triangle to be? "))
pascals_triangle(length)
