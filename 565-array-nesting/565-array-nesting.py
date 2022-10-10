class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        longest = 1
        seen = set()
        for i in range(len(nums)):
            count = 0
            while nums[i] not in seen:
                seen.add(nums[i])
                i = nums[i]
                count += 1
            longest = max(longest, count)
        
        return longest