class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used_num = {}
        maxLength = start = 0

        for n, l in enumerate(s):
            if l in used_num and start <= used_num[l]:
                start = used_num[l] + 1
            else:
                maxLength = max(maxLength, n - start + 1)

            used_num[l] = n
        return maxLength