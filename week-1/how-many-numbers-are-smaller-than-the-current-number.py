# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/

class Solution:
    def smallerNumbersThanCurrent(self, nums):
       
        num = nums[:]
        num.sort()
        
        lst= []
        for i in range(len(nums)):
            if i>1 and num[num.index(nums[i])] == num[num.index(nums[i])-1]:
                lst.append(lst[-1])
            else:
                lst.append(num.index(nums[i]))
                
        return lst
            
        