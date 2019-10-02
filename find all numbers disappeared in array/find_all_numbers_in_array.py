class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            new_i = abs(n) -1
            if nums[new_i] > 0:
                nums[new_i] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]