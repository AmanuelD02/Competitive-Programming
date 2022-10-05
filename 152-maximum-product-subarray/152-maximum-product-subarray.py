class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = 1, 1
        N = len(nums)
        ans = -float("inf")
        for i in range(len(nums)):
            j = N - 1 - i
            prevSum = prefix if prefix != 0 else 1
            prefix = nums[i] * prevSum
            

            sufSum = suffix if suffix != 0 else 1
            suffix = nums[j]* sufSum
            ans = max(ans,suffix, prefix)
        
        
        
        return ans
                           
            