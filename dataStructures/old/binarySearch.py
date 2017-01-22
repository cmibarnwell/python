def binarySearch(list, val):
	iLeft = 0
	iRight = len(list)

	while iLeft<iRight:
		iMid = (iLeft+iRight)//2
		if(val == list[iMid]):
			return iMid
		elif(val < list[iMid]):
			iRight = iMid-1
		else:
			iLeft = iMid+1
	return -1