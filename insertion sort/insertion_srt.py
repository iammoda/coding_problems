def binarySearch(array, target):
	return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
	if left > right:
		return -1
	mid = (left + right)// 2
	potentialMatch = array[mid]
	if target == potentialMatch:
		return mid
	elif target < potentialMatch:
		return binarySearchHelper(array, target, left, mid -1)
	else:
		return binarySearchHelper(array, target, mid + 1, right)