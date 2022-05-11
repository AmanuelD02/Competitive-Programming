class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        for i, j in zip(s,t):
            if i != j:
                return j
        return t[-1]