class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        N = len(nums)
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, N - 1
            while left < right:
                sum = nums[left] + nums[i] + nums[right]
                if sum >0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    lastLeft, lastRight = left, right
                    while left < right and nums[left] ==nums[lastLeft]: left += 1
                    while left < right and nums[right] == nums[lastRight]: right -= 1
        
        return ans
                    
