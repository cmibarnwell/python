print("Compound Interest :")

amount = input('1000')
amount = float(amount)
rate = input('5')
time = input('10')
time = float(time)
compoundTimes = input('4')
compoundTimes = float(compoundTimes)

total_amount = amount * ((1 + ((float(rate)/100))/4)**(compoundTimes*time))
print('\nTotal Amount = $%0.2f' %total_amount)
compound_interest = total_amount - amount
print('Compound Interest = $%0.2f' %compound_interest)
