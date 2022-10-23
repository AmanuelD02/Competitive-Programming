class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, prev, k):
            if i >= len(prices) or k == 0:
                return 0
            
            cont = dp(i + 1, prev, k)
            # If bought previously
            if prev:
                sell = prices[i] + dp(i + 1, not prev, k - 1)
                return max(cont, sell)
            
            buy = -prices[i] + dp(i + 1, not prev, k)
            
            return max(cont, buy)
        
        return dp(0, False, 2)
            
            