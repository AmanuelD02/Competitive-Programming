class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        diff = nums[-1] - nums[0]
        if diff ==0:
            return diff
        
        ans = diff
        
        for i in range(len(nums) - 1):
            ans += (nums[i] + diff - nums[-1])
        
        return ans
        