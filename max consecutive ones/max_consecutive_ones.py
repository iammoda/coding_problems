class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_counter = 0
        curr_counter = 0
        for num in nums:
            if num == 1:
                curr_counter += 1
            else:
                if curr_counter > prev_counter:
                    prev_counter = curr_counter
                curr_counter = 0
        return max(curr_counter, prev_counter)

