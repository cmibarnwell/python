def findPowerRule():
    expo = float(input("What is the exponent of the algebraic expression? "))
    if(expo%1==0):
        expo=int(expo)
    newExpo = (expo-1)    
    if(expo!=0 and expo != 1):
        expo= str(expo)
        newExpo= str(newExpo)
        print(expo+"x^"+ newExpo)
    elif(expo==1):
        print("1")
    else:
        print("0")
findPowerRule()
