class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_to_list = list(s)
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        i, j = 0, len(s) - 1

        while j > i:
            if str_to_list[i] not in vowels:
                i += 1
                continue
            if str_to_list[j] not in vowels:
                j -= 1
                continue

            str_to_list[i], str_to_list[j] = str_to_list[j], str_to_list[i]
            i += 1
            j -= 1

        return "".join(str_to_list)