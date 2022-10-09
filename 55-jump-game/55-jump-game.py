class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        N = len(nums)
        i = 0
        while i < N and max_jump < N:
            if i > max_jump:
                return False
            
            max_jump = max(max_jump, i+ nums[i])
            
            i += 1
        
        return True
            
        
                    
        