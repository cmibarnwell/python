#Multiplication Table 2 program written by Caleb Barnwell
#Computer Science, 11-15-15

n=int(input("Please input positive integer: "))

print("*|", end="\t")

for i in range(1, n+1):
    print(i, end="\t")
print()
print("---+"+"--------"*n)


for j in range(1, n+1):
    print(j,"|","\t",end="")
    for k in range(1, n+1):
        print(j*k, end="\t")
    print("\n")
