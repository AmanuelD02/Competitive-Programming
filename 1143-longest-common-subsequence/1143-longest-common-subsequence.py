class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(i,j):
            if i >= len(text1):
                return 0
            if j >= len(text2):
                return 0
            equal = t1 = t2 = 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            
            t1 = dp(i + 1, j)
            t2 = dp(i,j + 1)
            
            return max(equal, t1,t2)
        
        return dp(0,0)