class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        opening = 0
        for i, j in enumerate(s):
            if j == ')':
                if i ==0: continue
                if s[i -1] =='(':
                    dp[i] = 2 + dp[i - 2]
                elif  i - dp[i-1] - 1 >=0 and s[i -dp[i-1] -1] == '(':
                    dp[i] = dp[i-1] + dp[i - dp[i-1]-2] + 2
        
        return max(dp)
                
                