class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num_size = len(nums)
        
        nums_cost = list(zip(nums, cost))
        nums_cost.sort()
        
        prefix = [0] * num_size
        suffix = [0] * num_size
        totalCoin = 0
        totalCoin2 = 0

        for i in range(num_size -1, 0, -1):
            j= num_size - i - 1
            prefix[0] += (nums_cost[i][0] - nums_cost[0][0]) * nums_cost[i][1]
            totalCoin += nums_cost[i][1]
            
            suffix[-1] += (nums_cost[-1][0] - nums_cost[j][0]) * nums_cost[j][1]
            totalCoin2 += nums_cost[j][1]
        
        
        for i in range(1, num_size -1):
            j = num_size - i - 1
            prefix[i] = prefix[i-1] - (nums_cost[i][0] - nums_cost[i-1][0])* totalCoin
            totalCoin -= nums_cost[i][1]
            
            suffix[j] = suffix[j + 1] - (nums_cost[j + 1][0] - nums_cost[j][0]) * totalCoin2
            totalCoin2 -= nums_cost[j][1]
        
        return min([ suffix[i] + prefix[i] for i in range(num_size)])