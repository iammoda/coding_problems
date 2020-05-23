# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        swapped = head.next
        pre = ListNode(0)

        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            pre.next = nxt
            nxt.next = head
            head = head.next
            pre = nxt.next
        return swapped