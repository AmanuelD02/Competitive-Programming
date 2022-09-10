class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i,state,left):
            
            if left < 0 or i >= len(prices):
                return 0
            # Do Nothing state
            nothing = dp(i+1, state, left)
            #Do Sth State
            something = 0
            if state:
                something = prices[i] + dp(i+1, not state, left)
            
            else:
                something = dp(i+1, not state, left-1) - prices[i]
            
            return max(nothing, something)
        
        
        return dp(0, False, k)