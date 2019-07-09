class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head
        while curr:
            if curr and curr.next:
                curr.val, curr.next.val = curr.next.val, curr.val

            # check if the curr.next.next is there before moving it
            if curr.next:  # check if the 2nd node is not none, which means 3rd node is there
                curr = curr.next.next  # move curr to the 3rd node
            else:
                break
        return head

