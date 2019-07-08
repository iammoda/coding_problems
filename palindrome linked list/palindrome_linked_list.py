class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        if values == values[::-1]:
            return True
        else:
            return False