class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = len(digits) - 1
        remainder = 0
        new_digits = []
        digits[digit] += 1
        while digits[digit] >= 10:
            digits[digit] %= 10
            remainder = 1
            digit -= 1
            if digit >= 0:
                digits[digit] += remainder
                remainder = 0
            else:
                break
        if remainder == 1:
            new_digits.append(1)
            new_digits = new_digits + digits
        return new_digits if len(new_digits) > 0 else digits


