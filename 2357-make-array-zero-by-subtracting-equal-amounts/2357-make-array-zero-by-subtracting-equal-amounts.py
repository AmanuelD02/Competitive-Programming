class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        cur = ans = 0
        for num in nums:
            if num > cur:
                ans += 1
                cur = num
                
        return ans