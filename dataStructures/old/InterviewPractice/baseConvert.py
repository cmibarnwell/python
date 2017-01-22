def baseConvert(base2):
	base4 = ""
	temp = ""
	i = 1
	for num in base2:
		i += 1
		print(num)
		if(i%2 == 0):
			if(temp == "0" and num== "0"):
				base4 = base4 + "0"
			if(temp == "1" and num== "0"):
				base4 = base4 + "1" 
			if(temp == "0" and num== "1"):
				base4 = base4 + "2"
			if(temp == "1" and num=="1"):
				base4 = base4 + "3"
		temp = num
	return base4

print(baseConvert("1010101010"))