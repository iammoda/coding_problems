def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True


def breaksDirection(direction, previous, current):
    difference = current - previous
    # if direction > 0 == True
    if direction > 0:
        # return T/F depending on the difference
        return difference < 0
    return difference > 0


pass

def isMonotonic(array):
    isDecreasing = True
	isIncreasing = True
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			isIncreasing = False
		if array[i] > array[i - 1]:
			isDecreasing = False
	return isDecreasing or isIncreasing
    pass

