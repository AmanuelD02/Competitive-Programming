class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i >= len(nums)-1:
                return 0
            minMove = float("inf")
            for j in range(nums[i],0,-1):
                minMove = min(minMove, 1 + dp(i + j))
            
            
            return minMove
        
        return dp(0)