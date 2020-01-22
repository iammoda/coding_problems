class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen_letters = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in seen_letters:
                seen_letters[letter] = 1
            else:
                seen_letters[letter] += 1

        for letter in t:
            if letter not in seen_letters:
                return False
            else:
                seen_letters[letter] -= 1

        for val in seen_letters.values():
            if val != 0:
                return False

        return True