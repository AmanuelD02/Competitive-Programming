class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 5:
            return n
        
        dp = [1]
        p2 = p3 = p5 = 0
        for i in range(n -1):
            new_num = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            
            dp.append(new_num)
            if new_num == dp[p2] * 2:
                p2 += 1
            if new_num == dp[p3] * 3:
                p3 += 1
            if new_num == dp[p5] * 5:
                p5 += 1
        
        
        return dp[-1]
        
        