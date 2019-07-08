class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        number = x
        while number > 0:
            remainder = number % 10
            reverse = (reverse*10) + remainder
            number /= 10
        if reverse == x:
            return True
        else:
            return False