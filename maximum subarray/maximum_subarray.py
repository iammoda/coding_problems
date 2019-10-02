class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = res = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            res = max(res, sum)
        return res
