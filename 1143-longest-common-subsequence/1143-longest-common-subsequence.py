class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        
        @cache
        def dp(i, j):
            if i == N or j == M:
                return 0
            
            one = two = three = 0
            if text1[i] == text2[j]:
                one = 1 + dp(i + 1, j + 1)
            else:
                two = dp(i + 1, j)
                three = dp(i, j + 1)
            return max(one, two, three)
        
        
        return dp(0, 0)