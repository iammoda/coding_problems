def minHeightBst(array):
    return minHeightConstructor(array, None, 0, len(array)-1)

def minHeightConstructor(array, bst, leftIdx, rightIdx):
	if rightIdx < leftIdx:
		return
	midIdx = (leftIdx + rightIdx)//2
	newBstNode = BST(array[midIdx])
	if bst is None:
		bst = newBstNode
	else:
		if array[midIdx] < bst.value:
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right
	minHeightConstructor(array, bst, leftIdx, midIdx -1)
	minHeightConstructor(array, bst, midIdx +1, rightIdx)
	return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

