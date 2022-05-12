class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        actual =( len(nums) * (len(nums)+1)) //2
        for i in nums:
            res += i
        return actual - res