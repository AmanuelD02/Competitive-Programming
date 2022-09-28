class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse = True)
        
        @lru_cache(None)
        def dp(amount, i):
            if amount ==0: return 1
            if amount <0 or i >= len(coins): return 0
            
            return dp(amount-coins[i],i) + dp(amount,i+1)
        
        
        return dp(amount,0)