class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < 1:
                nums[-1], nums[i] = nums[i], nums[-1]
                i-=1
                nums.pop()
            i +=1
        
        if len(nums) ==0: return 1
        for i in range(len(nums)):
            val = abs(nums[i]) -1
            if val < len(nums):
                nums[val] = -1* abs(nums[val])
        for i in range(len(nums)):
            if nums[i] >0:
                return i +1
        return i + 2