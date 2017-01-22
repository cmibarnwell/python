def get_products_of_all_ints_except_at_index(arg):
	if(len(arg) > 1):
		return arg[0] * get_products_of_all_ints_except_at_index(arg[1:])
	else:
		return arg[0]
    
arg = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index(arg))
