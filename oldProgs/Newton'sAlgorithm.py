#Newton's Algorithm program written by Caleb Barnwell
#Computer Science, 10-11-15

def mySqrt(n):
    oldguess=n/2
    for i in range(n):
        newguess= (1/2)*(oldguess+(n/oldguess))
        oldguess=newguess
    print(newguess)

number=input("What number would you like to find the square root of? ")
number_int= int(number)
mySqrt(number_int)
