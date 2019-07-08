class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap = {}
        for a in A:
            try:
                hashmap[a]
            except KeyError:
                hashmap[a] = 1
            else:
                return a

        return None