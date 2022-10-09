class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        
        """
        nums.sort()
        closest_sum = float("inf")
        
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                
                if abs(target - closest_sum) > abs(target - curSum):
                    closest_sum = curSum

                if target - curSum  == 0:
                    return closest_sum
                if curSum > target:
                    right -= 1
                else:
                    left += 1
        
        return closest_sum
            