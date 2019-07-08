class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        keys = {"U": 1, "D": -1, "L": -1, "R": 1}
        x = 0
        y = 0
        i = 0
        move = 0

        for i in range(0, len(moves)):
            if moves[i] == "R" or moves[i] == "L":
                move = keys[moves[i]]
                x += move
                i += 1
            elif moves[i] == "U" or moves[i] == "D":
                move = keys[moves[i]]
                y += move
                i += 1

        if x == 0 and y == 0:
            return True
        else:
            return False