def balancedBrackets(string):
    openingB = "({["
	closingB = ")}]"
	matchingB = {")": "(", "}": "{", "]": "["}
	stack = []
	for char in string:
		if char in openingB:
			stack.append(char)
		elif char in closingB:
			if len(stack) == 0:
				return False
			if stack[-1] == matchingB[char]:
				stack.pop()
			else:
				return False
	return len(stack) == 0
    pass