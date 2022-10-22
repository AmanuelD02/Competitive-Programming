class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_size = len(word1)
        w2_size = len(word2)
        
        dp = [[0] * (w1_size + 1) for _ in range(w2_size + 1)]
        # BASE CASE
        for i in range(w1_size + 1):
            dp[-1][i] = w1_size - i
            
        for i in range(w2_size + 1):
            dp[i][-1] = w2_size - i
        
        for i in range(w2_size - 1, -1, -1):
            for j in range(w1_size - 1 , -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]