class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            mx = mn  = nums[i]
            for j in range(i, len(nums)):
                if mx < nums[j]:
                    mx = nums[j]
                if mn > nums[j]:
                    mn = nums[j]
                res += (mx - mn)
        
        return res
            