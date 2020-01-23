class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_letters = {}

        for letter in s:
            if letter not in seen_letters:
                seen_letters[letter] = 1
            else:
                seen_letters[letter] += 1

        for i in range(len(s)):
            if seen_letters[s[i]] == 1:
                return i

        return -1
