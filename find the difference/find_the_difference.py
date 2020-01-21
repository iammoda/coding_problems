class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        seen_letters = {}
        additional_lett = []
        for i in s:
            if i not in seen_letters:
                seen_letters[i] = 1
            else:
                seen_letters[i] += 1

        for i in t:
            if i not in seen_letters or seen_letters[i] == 0:
                additional_lett.append(i)
            elif i in seen_letters:
                seen_letters[i] -= 1

        return additional_lett[0] if len(additional_lett) > 0 else -1