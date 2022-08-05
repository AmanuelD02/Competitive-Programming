class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        @lru_cache(None)
        def dp(targ):
            if targ ==0:
                return 1
            
            no_ways = 0
            for num in nums:
                if targ - num >= 0:
                    no_ways += dp(targ - num) 
                    continue
                break
            
            return no_ways
        
        
        return dp(target)
        