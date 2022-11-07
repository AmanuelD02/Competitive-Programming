class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(s)
        m = len(g)
        g.sort()
        s.sort()
        
        satisfied_childrens = 0
        i = j = 0
        while i < n and j < m:
            if s[i] >= g[j]:
                satisfied_childrens += 1
                j += 1
            i += 1
        
        return satisfied_childrens
            
                
                
        