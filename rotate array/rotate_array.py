class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        current_idx = 0
        start_idx = 0
        numbers_shifted = 0
        while numbers_shifted < len(nums):
            current_idx = start_idx
            prev_num = nums[current_idx]
            while True:
                next_idx = (current_idx + k) % len(nums)
                temp = nums[next_idx]
                nums[next_idx] = prev_num
                prev_num = temp
                current_idx = next_idx

                numbers_shifted += 1
                if current_idx == start_idx:
                    break
            start_idx += 1

        return nums