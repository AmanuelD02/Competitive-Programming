class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: x[1] - x[0])
        res = 0
        print(costs)
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += costs[i][1]
            else:
                res += costs[i][0]
        
        return res