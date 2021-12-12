# https://leetcode.com/problems/largest-number/
class Solution:
    def largestNumber(self, nums) -> str:
        def compare(num1,num2):
            n1 = num1 +num2
            n2 = num2 + num1
            return int(n1) > int(n2)
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        for i in range(len(nums)):
            Max = i
            for j in range(i+1,len(nums)):
                if compare(nums[j], nums[Max]):
                    Max = j
            nums[i], nums[Max] = nums[Max], nums[i]
        # print(nums)
        if nums[0] =="0":
            return "0"
        return "".join(nums)
            
            
            
        
        
        
        
            
        