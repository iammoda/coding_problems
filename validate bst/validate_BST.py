
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return vbh (tree, float("-inf"), float("inf"))

def vbh(tree, minValue, maxValue):
	if tree is None:
		return True
	if tree.value >= maxValue or tree.value < minValue:
		return False
	LeftIsValid = vbh(tree.left, minValue, tree.value)
	return LeftIsValid and vbh(tree.right, tree.value, maxValue)