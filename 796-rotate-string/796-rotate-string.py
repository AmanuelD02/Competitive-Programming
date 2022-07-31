class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            # print(i, goal[:1] +goal[1:])
            if s == goal[i:] + goal[:i] :
                return True
        return False