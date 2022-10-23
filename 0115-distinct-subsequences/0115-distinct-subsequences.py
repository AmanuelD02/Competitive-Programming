class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_size, t_size = len(s), len(t)
        
        dp = [[0] * (s_size + 1) for _ in range(t_size + 1)]
        
        for i in range(s_size + 1):
            dp[-1][i] = 1
            
        for i in range(t_size - 1, -1, -1):
            for j in range(s_size - 1, -1, -1):
                if t[i] == s[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                dp[i][j] += dp[i][j + 1]
                
        return dp[0][0]