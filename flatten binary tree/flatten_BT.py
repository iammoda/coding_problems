class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    inOrderNodes = getInOrder(root, [])
	for i in range(0, len(inOrderNodes) -1):
		leftNode = inOrderNodes[i]
		rightNode = inOrderNodes[i +1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return inOrderNodes[0]

def getInOrder(root, array):
	if root is not None:
		getInOrder(root.left, array)
		array.append(root)
		getInOrder(root.right, array)
	return array


