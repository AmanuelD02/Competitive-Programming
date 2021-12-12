# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = current = 0
        two = len(nums)-1
        def swap(a,b):
            nums[a], nums[b] = nums[b] , nums[a]
            
        while(current<=two):
            # print(current, nums)
            if nums[current] ==0 and zero !=current:
                
                swap(zero,current)
                zero+=1
            elif nums[current] ==2:
                swap(two,current)
                two -=1
            else:
                current+=1
        
        
        
        