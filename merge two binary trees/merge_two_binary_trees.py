# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            new_node = TreeNode(t1.val + t2.val)
            new_node.left = self.mergeTrees(t1.left, t2.left)
            new_node.right = self.mergeTrees(t1.right, t2.right)
            return new_node
        else:
            return t1 or t2
