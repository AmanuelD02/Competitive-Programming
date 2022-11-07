class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len(nums) == 1 and k%2 ==1:
            return -1
        
        maxTile = -1
        for i in range(min(n, k -1)):
            maxTile = max(maxTile, nums[i])
        
        if n > k:
            maxTile = max(maxTile,nums[k])
        
        return maxTile