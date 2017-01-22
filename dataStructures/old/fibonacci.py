#Recursively
def fib(val):
	iA = 0
	iB = 1
	iCount = 0
	return _fib(iA, iB, val, iCount)

def _fib(iA, iB, val, iCount):
	if(iCount < val):
		iCount += 1
		temp = iA
		iA = iB
		iB += temp
		return _fib(iA, iB, val, iCount)
	else:
		return iA

print(fib(4))