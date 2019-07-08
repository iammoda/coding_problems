class Solution(object):
    def twoSum(self, nums, target):

        complementmap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in complementmap:
                return [complementmap[num], i]
            else:
                complementmap[target - num] = i
