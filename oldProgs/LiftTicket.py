#Lift Ticket Program written by Caleb Barnwell
#Computer Science, 11-22-15

def purchase_lift_ticket(budget):
    #Asks user for ticket type
    ticket_type=int(input("Which type of ticket do you choose? >> "))
    print()

    #Asks user for age
    age= int(input("How old are you? >> "))
    while True:
        if age>0:
            break
        else:
            print("Please insert a valid age.")
            age= int(input("How old are you? >> "))

    #Begins Calculations       
    adult=45
    senior=30
    junior=30
    if age >= 18:
        price=adult        
    elif age>= 66:
        price=senior        
    else:
        price=junior       

    if ticket_type == 2:
        mid_price= price/2
    elif ticket_type==1:
        mid_price= price
    else:
        print()
        print("Error: Unavailable integer entered")

    #Here the tax is calculated
    final_price=(mid_price*.05)+mid_price

    return final_price

#Shows user available options
def lift_types():
    print("1. One-Day Ticket")
    print("2. Half-Day Ticket")

#Runs the show
def create_ski_day_budget():
    #Finds out user's budget
    budget=int(input("What is today's budget in dollars? >> "))
    print()
    lift_types()
    print()
    final_price=purchase_lift_ticket(budget)
    print()
    #Performs calculations
    if final_price > budget:
        remaining_money=budget-final_price
        print("You were not in budget. Your final balance is: $",remaining_money)
    else:
        remaining_money=budget-final_price
        print("You were in budget. Your final balance is: $",remaining_money)

#executes program    
print("Welcome to Bridger Bowl!")
create_ski_day_budget()

