class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        left = 0
        MaxWind = 0
        right = 0
        total =0
        while(right<len(nums)):
            
            # print(window)
            total += nums[right]
            
            while total + k < nums[right] * (right- left +1):
                # print(left, right,total + k, nums[right] * (right- left +1) )
                total -= nums[left]
                left +=1
            
            MaxWind = max(right -left+ 1, MaxWind)
            right +=1
            
                
        return MaxWind
            
            
        