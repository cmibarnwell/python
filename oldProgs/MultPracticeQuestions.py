import random
def multPractice():
    print("Let's practice multiplication!")
    points=0
    while points<10:
        num1=random.randrange(1,10)
        num2=random.randrange(1,10)
        answer=int(input("%s*%s= " %(num1,num2)))
        if answer==num1*num2:
            points=points+1
            print("Correct! You have",points,"total points.")
            continue
        else:
            print("Incorrect. You have",points,"total points.")
            continue
    print("You got 10 correct answers. Good Job!")
multPractice()
