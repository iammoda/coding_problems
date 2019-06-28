class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        pi = 0
        for pi in range(0, len(A)):
            if A[pi] % 2 == 0:
                B.append(A[pi])
                pi +=1
        for pi in range (0, len(A)):
            if A[pi] %2 != 0:
                B.append(A[pi])
                pi+=1
        return (B)