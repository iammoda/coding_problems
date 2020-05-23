# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.maxDifference = 0
        self.helper(root)
        return False if self.maxDifference >= 2 else True
    def helper(self, root):
        if root is None:
            return 0
        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)
        self.maxDifference = max(self.maxDifference, abs(left_depth - right_depth))
        if self.maxDifference >= 2:
            return False
        return 1 + max(left_depth, right_depth)