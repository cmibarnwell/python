def quickSort(list):
	quickSortHelper(list, 0, len(list)-1)

def quickSortHelper(list, first, last):
	if first < last:
		splitpoint = partition(list, first, last)
		quickSortHelper(list, first, splitpoint -1)
		quickSortHelper(list, splitpoint +1, last)

def partition(list, first, last):
	iPivot = list[first]
	iLeft = first + 1
	iRight = last
	bDone = False

	while not bDone:
		while iLeft <= iRight and list[iLeft] <= iPivot:
			iLeft += 1
		while iRight >= iLeft and list[iRight] >= iPivot:
			iRight -= 1
		if(iRight < iLeft):
			bDone = True
		else:
			temp = list[iLeft]
			list[iLeft] = list[iRight]
			list[iRight] = temp
	
	temp = list[first]
	list[first] = list[iRight]
	list[iRight] = temp

	return iRight

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)