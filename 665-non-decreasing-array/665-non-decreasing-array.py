class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        isModified = False
        curMax = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if isModified:
                   return False 
                isModified = True

                if curMax > nums[i] and i!=1:
                    nums[i] = nums[i-1]
            curMax = max(curMax, nums[i-1])
        # print(nums)
        return True
                    