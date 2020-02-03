class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen_numbers = {}
        intersection = []

        for number in nums1:
            if number not in seen_numbers:
                seen_numbers[number] = 1
            else:
                seen_numbers[number] += 1

        for number in nums2:
            if number in seen_numbers:
                intersection.append(number)
                del seen_numbers[number]
            else:
                continue

        return intersection
