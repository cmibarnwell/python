def speedingTicketCost():
    mph_over=int(input("How many mph over the speed limit where you travelling?>> "))
    if mph_over<=10:
        print("Your suggested fine is: $20")
    elif 10<mph_over<=20:
        print("Your suggested fine is: $40")
    elif 20<mph_over<=30:
        print("Your suggested fine is: $70")
    else:
        print("Your suggested fine is: $100")

speedingTicketCost()
