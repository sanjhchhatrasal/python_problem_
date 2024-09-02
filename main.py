# Given an array of integers, where some elements may be duplicated, the task is to sort the array based on the frequency of each element. The element with the highest frequency should appear first, followed by the element with the next highest frequency, and so on. If two elements have the same frequency, they should appear in the order they first appeared in the array.


def frequencySorting():
	arr = list(map(int, input("Enter elements: ").split()))
	dict = {}
	for i in arr:
		if i in dict.keys():
			dict[i] += 1
		else:
			dict[i] = 1
	print(dict)
	sortedArray = []
	for key in sorted(dict, key = dict.get, reverse=True):
		sortedArray.extend([key] * dict[key])
	print("sorted array is: ", " ".join(map(str, sortedArray)))
	print(sortedArray)
	
frequencySorting()