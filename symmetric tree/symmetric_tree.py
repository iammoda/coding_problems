# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)
    def dfs(self, L, R):
        if L and R:
            return L.val == R.val and self.dfs(L.left, R.right) and self.dfs(L.right, R.left)
        return L == R