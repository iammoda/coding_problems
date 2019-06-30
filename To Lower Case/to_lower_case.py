class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        stack = [ord(x) for x in str]
        for i in range(0, len(stack)):
            if stack[i] > 64 and stack[i] < 91:
                stack[i] += 32
        lower = [chr(x) for x in stack]
        return ''.join(lower)
