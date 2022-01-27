nested_list = ['a', 'b', 'c', ['d', 'e', ['f',['1', '2', ['3', ['4']]],  'g'], 'h', 'y'], 'k', 'l']
flat_list = []

def Flatten(nested_list):
	for element in nested_list:
		if type(element) == list:
			Flatten(element)
		else:
			flat_list.append(element)
	return flat_list

print(Flatten(nested_list))