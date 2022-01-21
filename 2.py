from functools import reduce

def flat_list(start, target_list):
    while start < 1:
        yield reduce(lambda x, y: x + y, target_list)
        start += 1


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in flat_list(0, nested_list):
    print(item)
