def mergeSort(list):
	print("Split", list)
	if len(list)>1:
		iMid = len(list)//2
		leftM = list[:iMid]
		rightM = list[iMid:]

		mergeSort(leftM)
		mergeSort(rightM)

		i = 0
		j = 0
		k = 0
		while i < len(leftM) and j < len(rightM):
			if(leftM[i]< rightM[j]):
				list[k] = leftM[i]
				i += 1
			else:
				list[k] = rightM[j]
				j += 1
			k += 1

		while i < len(leftM):
			list[k] = leftM[i]
			i += 1
			k += 1

		while j < len(rightM):
			list[k] = rightM[j]
			j += 1
			k += 1
		print("Merge", list)

list = [54,26,93,17,77,31,44,55,20]
mergeSort(list)
print(list)