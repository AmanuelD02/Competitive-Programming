class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        d = f = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                f = d+1
            elif nums[i] < nums[i-1]:
                d = f+1
                
        return max(f, d)