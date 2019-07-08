class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        rev = 0
        if x < 0:
            x *= -1
            negative = True
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10
            if rev > 2 ** (32 - 1):
                return (0)
        if negative:
            return (-1 * rev)
        else:
            return (rev)
