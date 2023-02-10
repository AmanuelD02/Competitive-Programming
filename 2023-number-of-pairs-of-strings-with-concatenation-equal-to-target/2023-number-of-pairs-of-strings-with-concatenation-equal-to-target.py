class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        N = len(nums)
        count = 0
        
        for i in range(N):
            for j in range(0, N):
                if i == j: continue
                if target == nums[i] + nums[j]:
                    count += 1
                
        
        return count 
        