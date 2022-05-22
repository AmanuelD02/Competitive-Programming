class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(is_left):
            if is_left == 0:
                return 0
            
            best = amount + 1
            for coin in coins:
                if (is_left - coin) >=  0:
                    best = min(best, 1 + dp(is_left - coin))
            
            return best
        
        for i in range(1, amount):
            dp(i)
        ans = dp(amount)
        return ans if ans != amount + 1 else -1
            
        
            