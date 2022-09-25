class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N, res = len(nums), []
        bef,after = [1]*(N + 1), [1]*(N + 1)
        for i in range(1,N):
            if nums[i-1] >= nums[i]:
                bef[i] = bef[i-1] + 1
        for i in range(N-2,-1,-1):
            if nums[i] <= nums[i+1]:
                after[i] = after[i+1] + 1
        
        for i in range(k,N-k):
            if bef[i-1] >= k and after[i+1] >=k:
                res.append(i)
        return res
