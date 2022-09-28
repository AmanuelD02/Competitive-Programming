class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, amount):
            if i ==len(nums):
                return 1 if amount == target else 0

            total = 0
            total += dp(i + 1, amount - nums[i])
            total += dp(i + 1, amount + nums[i])
            
            return total
        
        
        return dp(0,0)