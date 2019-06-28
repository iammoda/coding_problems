#climbing stairs
class Solution(object):
    def climbStairs(self, n):
        return getStair(n)

#define function to create stairs
def getStair(n):
    #state base cases
    if n == 1:
        return 1
    elif n == 2:
        return 2
    #create array called bottom up, input base cases
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 2

    #finding distinct ways to climb the stairs using 1 or 2 steps; use array to store values
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]