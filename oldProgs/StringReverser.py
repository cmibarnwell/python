#String Reverser Program written by Caleb Barnwell
#Computer Science, 12-13-15

def stringReverser(word):
    if word=="":
        return word
    else:
        return stringReverser(word[1:]) + word[0]


revWord=input("What word would you like reversed? ")
print(stringReverser(revWord))


