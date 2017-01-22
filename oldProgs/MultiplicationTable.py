#Multiplication Table program written by Caleb Barnwell
#Computer Science, 11-8-15

print("  ", '\t', "1", '\t', "2", '\t', "3", '\t', "4", '\t', "5", '\t', "6", '\t', "7", '\t', "8", '\t', "9")     
print("  ", '\t', "---", '\t', "---", '\t', "---", '\t', "---", '\t', "---", '\t', "---", '\t', "---", '\t', "---", '\t', "---")

for x in range(1,10):        # generate values for columns
    print(x,"|" '\t', x*1,'\t',x*2,'\t',x*3,'\t',x*4,'\t',x*5,'\t',x*6,'\t',x*7,'\t',x*8,'\t',x*9)
