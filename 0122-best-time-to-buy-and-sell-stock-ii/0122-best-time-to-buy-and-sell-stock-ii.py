class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i,prev):
            if i>= len(prices):
                return 0
            # Bought Before
            cont = dp(i + 1,  prev)
            if prev:
                sell = prices[i] + dp(i+1, not prev)
                return max(sell, cont)
        
            buy = - prices[i] + dp(i + 1, not prev)
            return max(cont, buy)
        
        return dp(0, False)