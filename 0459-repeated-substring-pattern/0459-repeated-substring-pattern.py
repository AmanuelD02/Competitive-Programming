class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n):
            remaining = (n - i)//i
            if s[0:i]*(remaining + 1) == s:
                return True
            
        
        
        return False