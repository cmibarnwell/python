import random

class Best:

	def __init__(self):
		self.iBestScore = 0
		self.bestGuessM = []
		self.iChar = 0


def randString(iStrLen):
	sGuess= ""
	iGuess = random.randint(97,130)
	if iGuess == 123:
		sGuess+=" "
	elif iGuess == 124:
		sGuess+=chr(39)
	elif iGuess == 125:
		sGuess+="."
	elif iGuess == 126:
		sGuess+=":"
	elif iGuess == 127:
		sGuess+=";"
	elif iGuess == 128:
		sGuess+="/"
	elif iGuess == 129:
		sGuess+=","
	elif iGuess == 130:
		sGuess+=chr(34)
	else:
		sGuess+=chr(iGuess)	
	return sGuess

def goalCheck(sGiven, sGuess, iStrLen, best):
	if sGuess == sGiven[best.iBestScore]:
		best.bestGuessM.append(sGuess)
		best.iBestScore+=1
	return best


def begin(sGiven):
	best = Best()
	iTries = 0
	iBestScore = 0
	sGuess= randString(len(sGiven))
	iTries+=1
	best= goalCheck(sGiven, sGuess, len(sGiven), best)

	while(best.iBestScore is not (len(sGiven))):
		sGuess= randString(len(sGiven))
		iTries+=1
		best= goalCheck(sGiven, sGuess, len(sGiven), best)
		if iTries%1000 ==0 and iTries!=0:
			print("Tries: %d Best Score: %d Best Guess: %s" %(iTries, best.iBestScore, "".join(best.bestGuessM)))

	return "".join(best.bestGuessM)






def main():
	string = input()
	string = string.lower()
	print("done!",begin(string))
	#print(ord('"'))

if __name__ == "__main__":
	main()