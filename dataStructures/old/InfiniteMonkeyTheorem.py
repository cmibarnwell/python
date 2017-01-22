import random

class Best:

	def __init__(self):
		self.iBestScore = 0
		self.sBestGuess = None

	def getScore(self):
		return self.iBestScore

	def getGuess(self):
		return self.sBestGuess

	def setScore(self, new):
		self.iBestScore = new

	def setGuess(self, new):
		self.sBestGuess = new


def randString(iStrLen):
	sGuess= ""
	for i in range(iStrLen):
		iGuess = random.randint(97,123)
		if iGuess == 123:
			sGuess+=" "
		else:
			sGuess+=chr(iGuess)	
	return sGuess

def goalCheck(sGiven, sGuess, iStrLen, best):
	iScore = 0
	for i in range(iStrLen):
		if sGuess[i] == sGiven[i]:
			iScore+=1
	if(iScore >= best.iBestScore or best.iBestScore==0):
		best.iBestScore = iScore
		best.sBestGuess = sGuess
	return best


def begin(sGiven):
	best = Best()
	iTries = 0
	iBestScore = 0
	sGuess= randString(len(sGiven))
	iTries+=1
	best= goalCheck(sGiven, sGuess, len(sGiven), best)

	while(best.iBestScore != (len(sGiven))):
		sGuess= randString(len(sGiven))
		iTries+=1
		best= goalCheck(sGiven, sGuess, len(sGiven), best)
		if iTries%1000 ==0 and iTries!=0:
			print("Tries: %d Best Score: %d Best Guess: %s" %(iTries, best.iBestScore, best.sBestGuess))

	return best.sBestGuess






def main():
	print("done!",begin("caleb"))
	#print("Hello%sWorld"%(chr(32)))

if __name__ == "__main__":
	main()