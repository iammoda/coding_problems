class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        NewHead = new = ListNode("dummy")
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next= l2
                l2 = l2.next
            new = new.next
        new.next = l1 or l2
        return NewHead.next