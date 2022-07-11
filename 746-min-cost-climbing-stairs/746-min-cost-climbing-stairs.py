class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(cost):
                return 0
            
            one = cost[i] + dp(i + 1)
            two = cost[i] + dp(i + 2)
            
            return min(one, two)
        
        return min(dp(0), dp(1))