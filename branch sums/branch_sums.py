class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateSums(root, 0, sums)
    return sums


def calculateSums(node, runningSum, sums):
    if node is None:
        return sums

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    calculateSums(node.left, newRunningSum, sums)
    calculateSums(node.right, newRunningSum, sums)

