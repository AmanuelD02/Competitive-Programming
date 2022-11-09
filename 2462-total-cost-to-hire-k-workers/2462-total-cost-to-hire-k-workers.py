class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        rightMost = n - 1 - candidates
        leftMost =  candidates
        heap = []
        
        for i in range(n):
            
            if i < leftMost or i > rightMost:
                heappush(heap, [costs[i], i])

        total_cost = 0
   
        for _ in range(k):
            if heap:
                curr = heappop(heap)
                total_cost += curr[0]

                if leftMost <= rightMost:
                    if leftMost >= curr[1]:
                        heappush(heap, [costs[leftMost],leftMost])
                        leftMost += 1

                    elif rightMost <=  curr[1]:
                        heappush(heap, [costs[rightMost], rightMost])
                        rightMost -= 1
        
        return total_cost
    
            