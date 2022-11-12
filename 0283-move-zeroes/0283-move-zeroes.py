class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        n = len(nums)
        for num in nums:
            if num == 0:
                count_zero += 1
        
        if count_zero == 0 or count_zero == n:
            return nums
        
        i = 0
        
        for j, num in enumerate(nums):
            if num != 0:
                if i != j:
                    nums[j] = 0
                    
                nums[i] = num
                i += 1
        

            