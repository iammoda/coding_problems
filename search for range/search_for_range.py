def searchForRange(array, target):
    finalRange = [-1, -1]
	aBs(array, target, 0, len(array)-1, finalRange, True)
	aBs(array, target, 0, len(array)-1, finalRange, False)
	return finalRange

def aBs(array, target, left, right, finalRange, goLeft):
	if left > right:
		return
	mid = (left + right)//2
	if array[mid] < target:
		aBs(array, target, mid +1, right, finalRange, goLeft)
	elif array[mid] > target:
		aBs(array, target, left, mid -1, finalRange, goLeft)
	else:
		if goLeft:
			if mid == 0 or array[mid -1]!= target:
				finalRange[0] = mid
			else:
				aBs(array, target, left, mid -1, finalRange, goLeft)
		else:
			if mid == len(array) -1 or array[mid +1] != target:
				finalRange[1] = mid
			else:
				aBs(array, target, mid +1, right, finalRange, goLeft)

