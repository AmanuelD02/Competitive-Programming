class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i,num in enumerate(nums):
            if nums[stack[-1]] > num: stack.append(i)
        
        max_ramp = 0
        right = len(nums) -1
        while right >= 0 and stack:
            if right < stack[-1]: break
            if nums[stack[-1]] > nums[right]:
                right -= 1
            else:
                max_ramp = max(max_ramp, right- stack[-1])
                stack.pop()
        return max_ramp