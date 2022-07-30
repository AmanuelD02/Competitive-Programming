class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        left, right = 0 , len(nums)-1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                total += 1
                left +=1
                right -=1
            elif sum < k:
                left += 1
            else:
                right -=1
        
        return total
            