class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        
        @cache
        def dp(i, j):
            if i == N or j == M:
                return 0
            one = two = three = 0
            if word1[i] == word2[j]:
                one = 1 + dp(i + 1, j + 1)
            else:
                two = dp(i + 1, j)
                three = dp(i, j + 1)
            return max(one, two ,three)
            
        return N + M - 2* dp(0,0)