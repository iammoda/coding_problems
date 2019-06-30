class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pi = 0
        pj = pi + 1
        while pj<len(nums):
            if nums[pi] == nums[pj]:
                nums.remove(nums[pj])
            elif nums[pi] != nums[pj]:
                pj+=1
                pi+=1
            else:
                continue