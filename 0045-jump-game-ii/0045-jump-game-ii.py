class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = furthest = curEnd = 0
        
        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if i == curEnd:
                curEnd = furthest
                jumps += 1
        return jumps