class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump, N = 0, len(nums)

        for i in range(N):
            if i > max_jump:
                return False
            
            max_jump = max(max_jump, i+ nums[i])
            
            i += 1
        
        return True
            
        
                    
        