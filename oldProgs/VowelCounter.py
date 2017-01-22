#Vowel Counter Program written by Caleb Barnwell
#Computer Science, 12-6-15

phrase=input("Please input a phrase or word: ")

Aa=phrase.count("a")+phrase.count("A")
Ee=phrase.count("e")+phrase.count("E")
Ii=phrase.count("i")+phrase.count("I")
Oo=phrase.count("o")+phrase.count("O")
Uu=phrase.count("u")+phrase.count("U")
Yy=phrase.count("y")+phrase.count("Y")
total=Aa+Ee+Ii+Oo+Uu+Yy

print(total)


