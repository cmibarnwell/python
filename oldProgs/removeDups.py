#DuplicateRemover Program written by Caleb Barnwell
#Computer Science, 12-13-15

def removeDups(word):
    noDups=""
    for char in word:
        if char not in noDups:
            noDups=noDups+char
    return noDups
answer=str(input("What word would you like altered? "))
print(removeDups(answer))
