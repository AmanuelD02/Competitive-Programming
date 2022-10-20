class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHouse(houses):
            h1, h2 = 0 , 0
            for i in range(len(houses)):
                h1, h2 = max(houses[i] + h2, h1) ,h1
            return h1
        return max(nums[0] + robHouse(nums[2:-1]), robHouse(nums[1:]))
            