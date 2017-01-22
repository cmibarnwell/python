
import random
import string

list1=string.ascii_letters
randoCharNum=len(list1)
charSpan=random.randrange(1,randoCharNum)
randoChar=list1[charSpan]
lowRC=randoChar.lower()

def charGuess(char):
    word=input("Please input a word: ")
    lowWord=word.lower()
    charExist=lowWord.find(char)
    if charExist==-1:
        print("The character is not found within this word. Please try again.")
        charGuess(char)
    else:
        print("Character found within chosen word! The character was: "+char)

charGuess(lowRC)
