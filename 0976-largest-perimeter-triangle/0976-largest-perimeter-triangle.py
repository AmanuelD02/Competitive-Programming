class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        
        for i in range(0,n):
            for j in range(i + 1, n):
                a_b = nums[i] + nums[j]
                
                for k in range(j+1, n):
                    if a_b > nums[k] and nums[k] + nums[i] > nums[j] \
                        and nums[j] + nums[k] > nums[i]:
                        return a_b + nums[k]
                    break
        
        
        
        
        
        
        
        return 0