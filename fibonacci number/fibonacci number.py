class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        last_two = [0, 1]
        counter = 2
        while counter <= N:
            newFib = last_two[0] + last_two[1]
            last_two[0] = last_two[1]
            last_two[1] = newFib
            counter += 1

        return last_two[1] if N >= 1 else last_two[0]