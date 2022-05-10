class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        isMapped = set()
        for i, j in zip(s, t):
            if i in mapping:
                if mapping[i] != j: return False
            elif j in isMapped:
                return False
            isMapped.add(j)
                
            mapping[i] = j
        return True