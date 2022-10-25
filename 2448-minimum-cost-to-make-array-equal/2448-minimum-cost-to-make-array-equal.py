class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost = list(zip(nums, cost))
        nums_cost.sort()
        
        median = sum(cost) // 2
        prefix = 0
         
        for num, cst in nums_cost:
            prefix += cst
            if prefix >= median:
                return sum([abs(num - nums_cost[i][0]) * nums_cost[i][1] for i in range(len(nums))])