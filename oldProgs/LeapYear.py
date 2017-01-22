#Leap Year program written by Caleb Barnwell
#Computer Science, 11-01-15

year= int(input("Please input a year: "))

if year % 4 == 0 and year%100!=0 or year % 400 ==0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")

