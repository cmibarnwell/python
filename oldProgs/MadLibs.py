#Ad Libs(Final Program) written by Caleb Barnwell
#Computer Science, 1-7-15

#Sets introductory values, and imports necessary modules

import random
import sys
score=0
a=1
b=2
c=3

story=0

#The next 3 functions set the stories up for Ad Libs
def adLib1():
    noun1=input("Please input a plural noun of your choice: ")
    noun2=input("Please input a place of your choice: ")
    noun3=input("Please input a noun of your choice: ")
    noun4=input("Please input a plural noun of your choice: ")
    noun5=input("Please input a noun of your choice: ")
    adj1=input("Please input an adjective of your choice: ")
    verb1=input("Please input a verb of your choice: ")
    num1=input("Please input a number of your choice: ")
    adj2=input("Please input an adjective of your choice: ")
    bp1=input("Please input a body part of your choice: ")
    verb2=input("Please input a verb of your choice: ")
    story1= "Two "+noun1+", both alike in dignity, In fair "+noun2+", where we lay our scene, From ancient "+noun3+" break to new mutiny, Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes A pair of star-cross`d "+noun4+" take their life; Whole misadventured piteous overthrows Do with their "+noun5+" bury their parents` strife. The fearful passage of their "+adj1+" love, And the continuance of their parents` rage, Which, but their children`s end, nought could "+verb1+", Is now the "+num1+" hours` traffic of our stage; The which if you with "+adj2+" "+bp1+" attend, What here shall "+verb2+", our toil shall strive to mend."
    return story1

def adLib2():

    Noun1=input("Please input a noun of your choice: ")
    Food1=input("Please input a food of your choice: ")
    Food2=input("Please input a food of your choice: ")
    Verb1=input("Please input a verb of your choice: ")
    Adverb1=input("Please input an adverb of your choice: ")
    Adjective1=input("Please input an adjective of your choice: ")
    Noun2=input("Please input a plural noun of your choice: ")
    Color1=input("Please input a color of your choice: ")
    Verb2=input("Please input a verb of your choice: ")
    Verb3=input("Please input a verb of your choice: ")
    Noun3=input("Please input a noun of your choice: ")
    Name1=input("Please input a female name of your choice: ")
    Noun4=input("Please input a plural noun of your choice: ")

    story2= "Picture yourself in a "+Noun1+" on a river, With "+Food1+" trees and "+Food2+" skies. Somebody calls you, you "+Verb1+" quite "+Adverb1+", A girl with "+Adjective1+" eyes. Cellophane "+Noun2+" of "+Color1+" and green, "+Verb2+" over your head. "+Verb3+" for the girl with the "+Noun3+" in her eyes, And she`s gone. "+Name1+" in the sky with "+Noun4+"... " +Name1+ " in the sky with "+Noun4+"... "+Name1+" in the sky with "+Noun4+"..."
    return story2

def adLib3():
    color1=input("Please input a color of your choice: ")
    superlative1=input("Please input a superlative of your choice: ")
    adj1=input("Please input a plural adjective of your choice: ")
    bp1=input("Please input a plural body part of your choice: ")
    bp2=input("Please input a body part of your choice: ")
    noun1=input("Please input a noun of your choice: ")
    animal1=input("Please input a plural animal of your choice: ")
    adj2=input("Please input an adjective of your choice: ")
    adj3=input("Please input an adjective of your choice: ")
    adj4=input("Please input an adjective of your choice: ")

    story3= "The "+color1+" Dragon is the "+superlative1+" Dragon of all. It has "+adj1+" "+bp1+", and a "+bp2+" shaped like a "+noun1+". It loves to eat "+animal1+", although it will feast on nearly anything. It is "+adj2+" and "+adj3+". You must be "+adj4+" around it, or you may end up as it`s meal!"
    return story3

#Used when finishing program
def salutations():
    print("Bye!")

#Conclusive function
def completionInquire():
    print("Congratulations! You have composed all stories")
    stop1=6
    while stop1==6:
        retry=input("Play again (y/n)? ")
        if retry=="y":
            randStoryPicker(score,a,b,c)
        elif retry=="n":
            print("Thanks for playing!")            
            salutations()
            stop1=3
            sys.exit()
        else:
            print("I don't understand.")
            continue

#Sets random order for stories
def storyNumGenerator(a,b,c):
    storynum=random.choice([a,b,c])
    return storynum

#Main Function, Executes all and uses recursive functions
def randStoryPicker(score,a,b,c):
    print("You have composed",score,"stories.")
    while (a+b+c)>=-5:       
        story=storyNumGenerator(a,b,c)
        if story<=0:
            story=storyNumGenerator(a,b,c)
            continue
        else:        
            score=score+1
            if story==1:
                story1=adLib1()
                print(story1)
                a=-1
            elif story==2:
                story2=adLib2()
                print(story2)
                b=-2
            else:
                story3=adLib3()
                print(story3)
                c=-3        
        randStoryPicker(score,a,b,c)
        break
    completionInquire()

#Executes main program, intro phrase
print("Welcome to the Ad Libs program by Caleb Barnwell!")
randStoryPicker(score,a,b,c)


