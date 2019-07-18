# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return inorder
            else:
                node = stack.pop()
                inorder.append(node.val)
                print inorder
                root = node.right
        return inorder

