def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	index1 = 0
	index2 = 0
	smallest = float("inf")
	closest = float("inf")
	smallestPair = []
	while index1 < len(arrayOne) and index2 < len(arrayTwo):
		p1 = arrayOne[index1]
		p2 = arrayTwo[index2]
		if p1 > p2:
			closest = p1 - p2
			index2 += 1
		elif p2 > p1:
			closest = p2 - p1
			index1 += 1
		else:
			return [p1, p2]
		if smallest > closest:
			smallest = closest
			smallestPair = [p1, p2]
	return smallestPair