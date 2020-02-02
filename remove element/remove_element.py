class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        char = 0
        for d in range(len(nums)):
            if nums[d] != val:
                 nums[char] = nums[d]
                 char+=1
        return char