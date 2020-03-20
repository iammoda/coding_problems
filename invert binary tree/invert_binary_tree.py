def invertBinaryTree(tree):
    if tree is None:
        return
    swapTreeNodes(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapTreeNodes(tree):
    tree.left, tree.right = tree.right, tree.left


pass