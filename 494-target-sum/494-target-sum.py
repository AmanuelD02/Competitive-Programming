class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total: return 0
        
        dp = [0] * (2*total + 1)
        dp[total] = 1
        for i, num in enumerate(nums):
            next = [0] * (2*total + 1)
            for s in range(2*total+1):
                if dp[s] != 0:
                    next[s + num] += dp[s]
                    next[s - num] += dp[s]

            dp = next
        
        return dp[total + target]

            
        