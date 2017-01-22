#Final Exam written by Caleb Barnwell
#Computer Science, 1-13-15

def question():
    ans=input("Do you want to continue? ")
    realAns=ans.lower()
    
    if realAns=="g" or realAns=="go":
        question()
    elif realAns=="s" or realAns=="stop":
        print("Program Stopped")
    else:
        print("I don't understand")
        question()

question()
